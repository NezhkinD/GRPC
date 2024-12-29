import grpc
from concurrent import futures
import time
import services_pb2
import services_pb2_grpc
import random


class ReviewService(services_pb2_grpc.Review):
    def Create(self, request, context):
        return services_pb2.NewDataResponse(
            message=f"Пользователь с id {request.user_id}, оставил отзыв к заказу с id {request.order_id}, '{request.message}' и оценкой {request.rating}",
            id=random.randint(0, 125),
            status=True,
            user_id=request.user_id
        )

    def Get(self, request, context):
        return services_pb2.ReviewResponse(
            order_id=random.randint(0, 125),
            message=f"Отзыв #{request.id}: Спасибо, все прошло отлично!",
            rating=10,
            user_id=random.randint(0, 125)
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_ReviewServicer_to_server(ReviewService(), server)
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
