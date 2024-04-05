import signal
import threading
import time
from typing import List

import requests
from config import (
    DeviceIp,
    ErrorSleepInterval,
    MatrixAuth,
    MaxEventsFetch,
    PositionCacheMap,
    PositionPortMap,
    PositionROCSeqMap,
    PositionUriMap,
    SleepInterval,
    Position,
)
from parse import parseEvents
from rpc import onMatrixScan
import socket


def listenPosition(position: Position, ev: threading.Event):
    print(f"Listening for position: {position}")
    uri = PositionUriMap[position]
    listenPort = PositionPortMap[position]

    listenUri = (
        f"{uri}/device.cgi/tcp-events?action=getevent"
        f"&ipaddress={DeviceIp}&port={listenPort}&keep-live-events=1"
        f"&format=xml"
    )

    # Create a tcp socket to listener on port port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", listenPort))
    server.listen()

    while True:
        client, address = server.accept()
        data = client.recv(1024)
        # Process the received data
        # ...
        client.close()

    # TODO: Implement, should be a infinite loop with error handling and retries
    # Based on output, call
    matrixId = 0  # The person id
    onMatrixScan(matrixId, position)


def pollPosition(position: Position, ev: threading.Event):
    uri = PositionUriMap[position]
    cache = PositionCacheMap[position]

    pollUriBase = f"{uri}/device.cgi/events?action=getevent&no-of-events={MaxEventsFetch}&format=xml"
    configRoc, configSeq = PositionROCSeqMap[position]
    lastROC = max(configRoc, cache.get("lastROC", 0))
    lastSeqNo = max(configSeq, cache.get("lastSeqNo", 1))

    # Skip to the last known event
    while not ev.is_set():
        pollUri = f"{pollUriBase}&roll-over-count={lastROC}&seq-number={lastSeqNo}"
        try:
            resp = requests.get(pollUri, auth=MatrixAuth)
        except Exception as e:
            print(f"{position} Error: {e}")
            time.sleep(ErrorSleepInterval)
            continue
        events = parseEvents(resp.text)

        if len(events) == 0:
            break

        lastROC = events[-1].rollOverCount
        lastSeqNo = events[-1].seqNo + 1
        cache["lastROC"] = lastROC
        cache["lastSeqNo"] = lastSeqNo

        print(f"{position} Skipping Events: {len(events)} from {lastROC}:{lastSeqNo}")

    if not ev.is_set():
        print(f"Polling for position: {position} from {lastROC}:{lastSeqNo}")
    # Start polling
    while not ev.is_set():
        try:
            pollUri = f"{pollUriBase}&roll-over-count={lastROC}&seq-number={lastSeqNo}"
            resp = requests.get(pollUri, auth=MatrixAuth)
            events = parseEvents(resp.text)

            if len(events) > 0:
                print(f"{position} Events: {len(events)}")
                for event in events:
                    print(f"{position} EventId: {event.eventId}")
            else:
                print(f"{position} No Events")
                time.sleep(SleepInterval)
                continue

            lastROC = events[-1].rollOverCount
            lastSeqNo = events[-1].seqNo + 1
            cache["lastROC"] = lastROC
            cache["lastSeqNo"] = lastSeqNo

            for event in events:
                onMatrixScan(event.eventId, position)

            time.sleep(SleepInterval)

        except Exception as e:
            print(f"{position} Error: {e}")
            time.sleep(ErrorSleepInterval)


def listenAll():
    threads: List[threading.Thread] = []
    event = threading.Event()

    signal.signal(signal.SIGINT, lambda sig, frame: event.set())
    signal.signal(signal.SIGTERM, lambda sig, frame: event.set())

    for position in [
        Position.Position_weapon,
        Position.Position_ammo,
        Position.Position_clearing,
    ]:
        t = threading.Thread(target=pollPosition, args=(position, event))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# Run python listen.py
if __name__ == "__main__":
    listenAll()
