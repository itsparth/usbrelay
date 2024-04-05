from dataclasses import dataclass

from diskcache import Cache
import grpc

from root.message_pb2 import Position


@dataclass
class PinMap:
    buzzer: int
    red: int
    green: int


PositionPinMap: dict[Position, PinMap] = {
    Position.Position_weapon: PinMap(buzzer=1, red=2, green=3),
    Position.Position_ammo: PinMap(buzzer=4, red=5, green=6),
    Position.Position_clearing: PinMap(buzzer=7, red=8, green=9),
}

PositionUriMap: dict[Position, str] = {
    Position.Position_weapon: "http://localhost:5000",
    Position.Position_ammo: "http://localhost:5001",
    Position.Position_clearing: "http://localhost:5002",
}

DefaultDuration: float = 1

GrpcServerAddress: str = "localhost:50051"

GrpcChannel = grpc.insecure_channel(GrpcServerAddress)

DeviceIp: str = "192.168.22.55"

PositionPortMap: dict[Position, int] = {
    Position.Position_weapon: 5000,
    Position.Position_ammo: 5001,
    Position.Position_clearing: 5002,
}


PositionCacheMap: dict[Position, Cache] = {
    Position.Position_weapon: Cache("weapon"),
    Position.Position_ammo: Cache("ammo"),
    Position.Position_clearing: Cache("clearing"),
}

MaxEventsFetch = 100
