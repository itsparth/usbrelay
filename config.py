from dataclasses import dataclass
import enum
from typing import Dict

from diskcache import Cache
import grpc

from root.message_pb2 import Position


@dataclass
class PinMap:
    buzzer: int
    red: int
    green: int


class PositionEnum(enum.IntEnum):
    weapon = 1
    ammo = 2
    clearing = 3

    @property
    def protoEnum(self) -> Position:
        return {
            PositionEnum.weapon: Position.Position_weapon,
            PositionEnum.ammo: Position.Position_ammo,
            PositionEnum.clearing: Position.Position_clearing,
        }[self]


PositionPinMap: Dict[Position, PinMap] = {
    PositionEnum.weapon: PinMap(buzzer=1, red=2, green=3),
    PositionEnum.ammo: PinMap(buzzer=4, red=5, green=6),
    PositionEnum.clearing: PinMap(buzzer=7, red=8, green=9),
}

PositionUriMap: Dict[Position, str] = {
    PositionEnum.weapon: "http://localhost:5000",
    PositionEnum.ammo: "http://localhost:5001",
    PositionEnum.clearing: "http://localhost:5002",
}

DefaultDuration: float = 1

GrpcServerAddress: str = "localhost:8080"

GrpcChannel = grpc.insecure_channel(GrpcServerAddress)

DeviceIp: str = "192.168.22.55"

PositionPortMap: Dict[Position, int] = {
    PositionEnum.weapon: 5000,
    PositionEnum.ammo: 5001,
    PositionEnum.clearing: 5002,
}


PositionCacheMap: Dict[Position, Cache] = {
    PositionEnum.weapon: Cache("cache/weapon"),
    PositionEnum.ammo: Cache("cache/ammo"),
    PositionEnum.clearing: Cache("cache/clearing"),
}

MaxEventsFetch = 100

SleepInterval = 1
ErrorSleepInterval = 3
