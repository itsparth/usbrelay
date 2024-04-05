import threading
import time

import requests
from config import (
    DeviceIp,
    MaxEventsFetch,
    PositionCacheMap,
    PositionPortMap,
    PositionUriMap,
)
from parse import parseEvents
from root.message_pb2 import Position
from rpc import onMatrixScan
import socket


def listenPosition(position: Position):
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
    server.bind((DeviceIp, listenPort))
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
    lastROC = cache.get("lastROC", 0)
    lastSeqNo = cache.get("lastSeqNo", 0)

    # Skip to the last known event
    while True:
        pollUri = f"{pollUriBase}&roll-over-count={lastROC}&seq-number={lastSeqNo}"
        resp = requests.get(pollUri)
        events = parseEvents(resp.text)

        if len(events) == 0:
            break

        lastROC = events[-1].rollOverCount
        lastSeqNo = events[-1].seqNo
        cache["lastROC"] = lastROC
        cache["lastSeqNo"] = lastSeqNo

    # Start polling
    while not ev.is_set():
        try:
            pollUri = f"{pollUriBase}&roll-over-count={lastROC}&seq-number={lastSeqNo}"
            resp = requests.get(pollUri)
            events = parseEvents(resp.text)

            for event in events:
                onMatrixScan(event.eventId, position)
                lastROC = event.rollOverCount
                lastSeqNo = event.seqNo
                cache["lastROC"] = lastROC
                cache["lastSeqNo"] = lastSeqNo

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)


def listenAll():
    threads: list[threading.Thread] = []
    for position in [
        Position.Position_weapon,
        Position.Position_ammo,
        Position.Position_clearing,
    ]:
        t = threading.Thread(target=pollPosition, args=(position,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# Run python listen.py
if __name__ == "__main__":
    listenAll()
