import grpc
from config import DefaultDuration, GrpcChannel, PositionPinMap
from relay import turnOnForAsync
from root.message_pb2 import FlowsOnScanRequest, FlowsOnScanResponse, Position
from root.service_pb2_grpc import FlowsServiceStub


def onFlowsScan(matrixId: int, position: Position) -> FlowsOnScanResponse:
    return FlowsServiceStub(GrpcChannel).flowsOnScan(
        FlowsOnScanRequest(matrixId=matrixId, position=position)
    )


# Primary method to be called
def onMatrixScan(matrixId: int, position: Position):
    resp = onFlowsScan(matrixId, position)
    pinMap = PositionPinMap[position]

    if resp.buzzer:
        turnOnForAsync(pinMap.buzzer, DefaultDuration)
    if resp.red:
        turnOnForAsync(pinMap.red, DefaultDuration)
    if resp.green:
        turnOnForAsync(pinMap.green, DefaultDuration)
