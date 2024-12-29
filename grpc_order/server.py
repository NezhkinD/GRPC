import grpc
from concurrent import futures
import time
import services_pb2
import services_pb2_grpc
import random


class OrderService(services_pb2_grpc.Order):
    def Create(self, request, context):
        return services_pb2.NewDataResponse(
            message=f"Заказ для пользователя с id {request.user_id} создан",
            id=random.randint(0, 125),
            status=True,
            user_id=request.user_id
        )

    def Get(self, request, context):
        return services_pb2.OrderResponse(
            name=f"Заказ на доставку товара #{request.id}",
            user_id=random.randint(0, 125),
            status="доставлено",
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_OrderServicer_to_server(OrderService(), server)
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
