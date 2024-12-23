import grpc
from concurrent import futures
import recommendations_pb2
import recommendations_pb2_grpc


class RecommendationService(recommendations_pb2_grpc.RecommendationServiceServicer):
    def Recommend(self, request, context):
        # Implement your recommendation logic here
        # For simplicity, returning a static list of recommendations
        recommendations = ["Book 1", "Book 2", "Book 3"]
        return recommendations_pb2.RecommendationResponse(recommendations=recommendations)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationServiceServicer_to_server(RecommendationService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Recommendation service started...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
