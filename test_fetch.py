import signal
import threading
import time
from typing import List

import requests
from config import (
    DeviceIp,
    ErrorSleepInterval,
    MaxEventsFetch,
    PositionCacheMap,
    PositionPortMap,
    PositionUriMap,
    SleepInterval,
    Position,
)
from parse import parseEvents
from rpc import onMatrixScan
import socket


def pollPositionDebug(position: Position):
    uri = PositionUriMap[position]
    cache = PositionCacheMap[position]

    pollUriBase = f"{uri}/device.cgi/events?action=getevent&no-of-events={MaxEventsFetch}&format=xml"
    lastROC = cache.get("lastROC", 0)
    lastSeqNo = cache.get("lastSeqNo", 0)

    pollUri = f"{pollUriBase}&roll-over-count={lastROC}&seq-number={lastSeqNo}"

    print(pollUri)
    resp = requests.get(pollUri)
    print(resp.text)

    events = parseEvents(resp.text)

    print("Count", len(events))


# Run python listen.py
if __name__ == "__main__":
    pollPositionDebug(Position.Position_ammo)
