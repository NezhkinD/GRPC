import grpc
from concurrent import futures
import time
import services_pb2
import services_pb2_grpc
import random

class UserService(services_pb2_grpc.User):
    def Create(self, request, context):
        hidePassword = self.hidePassword(request.password)
        return services_pb2.NewDataResponse(
            message=f"Пользователь, {request.name} и паролем {hidePassword}, успешно зарегистрирован!",
            id=random.randint(1, 9999),
            status=True
        )

    def Auth(self, request, context):
        hidePassword = self.hidePassword(request.password)
        return services_pb2.AuthResponse(
            message=f"Пользователь, {request.name} и паролем  {hidePassword} успешно авторизирован!",
            status=True
        )

    def hidePassword(self, password):
        return '*' * len(password)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_UserServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server started on port 50051.")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
