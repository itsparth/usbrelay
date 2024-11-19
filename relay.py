# import usbrelay_py
import time
import threading
import requests

from config import RelayIp

# count = usbrelay_py.board_count()
# print("Count: ", count)

# boards = usbrelay_py.board_details()
# print("Boards: ", boards)


# def turnOn(index: int):
#     board = boards[0]
#     result = usbrelay_py.board_control(board[0], index, 1)
#     print(f"Turn on: {index} result {result}")


# def turnOff(index: int):
#     board = boards[0]
#     result = usbrelay_py.board_control(board[0], index, 0)
#     print(f"Turn off: {index} result {result}")


def turnOn(index: int):
    # get request
    requests.get(f"http://${RelayIp}/control?pin=${index}&state=HIGH")
    print(f"Turn on: {index}")


def turnOff(index: int):
    requests.get(f"http://{RelayIp}/control?pin=${index}&state=LOW")
    print(f"Turn off: {index}")


def turnOnFor(index: int, duration: float):
    turnOn(index)
    time.sleep(duration)
    turnOff(index)


def turnOnForAsync(index: int, duration: float):
    t = threading.Thread(target=turnOnFor, args=(index, duration))
    t.start()
