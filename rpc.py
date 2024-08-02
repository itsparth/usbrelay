from config import DefaultDuration, GrpcChannel, Position, PositionPinMap
from relay import turnOnForAsync
from krypton.cisf.message_pb2 import FlowsOnScanRequest, FlowsOnScanResponse
from krypton.cisf.service_pb2_grpc import FlowsServiceStub


def onFlowsScan(matrixId: str, position: Position) -> FlowsOnScanResponse:
    return FlowsServiceStub(GrpcChannel).flowsOnScan(
        FlowsOnScanRequest(biometricsId=int(matrixId), position=position.grpc)
    )


# Primary method to be called
def onMatrixScan(matrixId: str, position: Position):
    resp = onFlowsScan(matrixId, position)
    pinMap = PositionPinMap[position]

    if resp.green:
        turnOnForAsync(pinMap.green, DefaultDuration)
        return
    if resp.buzzer:
        turnOnForAsync(pinMap.buzzer, DefaultDuration)
    if resp.red:
        turnOnForAsync(pinMap.red, DefaultDuration)
