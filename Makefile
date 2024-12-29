.PHONY: build up down restart build_up dbu recreate_proto clean_proto proto proto_helloworld proto_create docker_fix

dbu: recreate_proto down build_up
build_up: build up
recreate_proto: clean_proto proto_create copy_proto

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

restart:
	docker-compose restart

copy_proto:
	cp -rf ./proto/services_pb2.py ./grpc_order/services_pb2.py
	cp -rf ./proto/services_pb2.py ./grpc_review/services_pb2.py
	cp -rf ./proto/services_pb2.py ./grpc_user/services_pb2.py
	cp -rf ./proto/services_pb2_grpc.py ./grpc_user/services_pb2_grpc.py
	cp -rf ./proto/services_pb2_grpc.py ./grpc_review/services_pb2_grpc.py
	cp -rf ./proto/services_pb2_grpc.py ./grpc_order/services_pb2_grpc.py

clean_proto:
	rm -f ./proto/services_pb2.py
	rm -f ./proto/services_pb2_grpc.py

proto_create:
	python3 -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/services.proto

docker_fix:
	docker container prune