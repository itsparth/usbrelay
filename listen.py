import threading
from config import PositionUriMap
from root.message_pb2 import Position
from rpc import onMatrixScan


def listenPosition(position: Position):
    print(f"Listening for position: {position}")
    uri = PositionUriMap[position]
    # TODO: Implement, should be a infinite loop with error handling and retries
    # Based on output, call
    matrixId = 0  # The person id
    onMatrixScan(matrixId, position)


def listenAll():
    threads: list[threading.Thread] = []
    for position in [
        Position.Position_weapon,
        Position.Position_ammo,
        Position.Position_clearing,
    ]:
        t = threading.Thread(target=listenPosition, args=(position,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# Run python listen.py
if __name__ == "__main__":
    listenAll()
