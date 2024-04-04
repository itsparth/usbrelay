pip install grpcio-tools
python -m grpc_tools.protoc -Igrpc/ --python_out=. --pyi_out=. --grpc_python_out=. grpc/root/service.proto grpc/root/message.proto