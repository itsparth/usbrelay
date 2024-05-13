from config import Position
from rpc import onMatrixScan


biometricsId = ""
position = 0

while True:
    prefilStr = " [or enter to use {biometricsId}]" if biometricsId != "" else ""
    print(f"Enter biometricsId{prefilStr}:", end="")
    biometricsId = input()

    prePosStr = " [or enter to use {position}]" if position != 0 else ""
    print(f"Enter position (1/2/3){prePosStr}:", end="")
    position = int(input())

    onMatrixScan(biometricsId, Position(position))
