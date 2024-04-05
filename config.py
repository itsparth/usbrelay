from dataclasses import dataclass
import enum
from typing import Dict

from diskcache import Cache
import grpc

from root.message_pb2 import Position as GrpcPosition


@dataclass
class PinMap:
    buzzer: int
    red: int
    green: int


class Position(enum.Enum):
    Position_weapon = 1
    Position_ammo = 2
    Position_clearing = 3

    @property
    def grpc(self):
        return {
            Position.Position_weapon: GrpcPosition.Position_weapon,
            Position.Position_ammo: GrpcPosition.Position_ammo,
            Position.Position_clearing: GrpcPosition.Position_clearing,
        }[self]


PositionPinMap: Dict[Position, PinMap] = {
    Position.Position_weapon: PinMap(buzzer=1, red=2, green=3),
    Position.Position_ammo: PinMap(buzzer=4, red=5, green=6),
    Position.Position_clearing: PinMap(buzzer=7, red=8, green=9),
}

PositionUriMap: Dict[Position, str] = {
    Position.Position_weapon: "http://192.168.2.11:80",
    Position.Position_ammo: "http://192.168.2.12:80",
    Position.Position_clearing: "http://192.168.2.13:80",
}

DefaultDuration: float = 1

GrpcServerAddress: str = "localhost:8080"

GrpcChannel = grpc.insecure_channel(GrpcServerAddress)

DeviceIp: str = "192.168.22.55"

PositionPortMap: Dict[Position, int] = {
    Position.Position_weapon: 5000,
    Position.Position_ammo: 5001,
    Position.Position_clearing: 5002,
}


PositionCacheMap: Dict[Position, Cache] = {
    Position.Position_weapon: Cache("cache/weapon"),
    Position.Position_ammo: Cache("cache/ammo"),
    Position.Position_clearing: Cache("cache/clearing"),
}

MaxEventsFetch = 100

SleepInterval = 1
ErrorSleepInterval = 3


MatrixAuth = ("admin", "1234")
