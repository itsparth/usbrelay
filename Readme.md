pip install grpcio-tools
python -m grpc_tools.protoc -Igrpc/ --python_out=. --pyi_out=. --grpc_python_out=. grpc/root/service.proto grpc/root/message.proto

python -m grpc_tools.protoc -I /home/parth/Work/astra/astra_proto/proto --python_out=. --pyi_out=. --grpc_python_out=. /home/parth/Work/astra/astra_proto/proto/krypton/airport/service.proto /home/parth/Work/astra/astra_proto/proto/krypton/airport/message.proto