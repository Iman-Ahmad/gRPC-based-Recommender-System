import grpc
import recommendations_pb2
import recommendations_pb2_grpc


def get_recommendations(user_id, category):
    channel = grpc.insecure_channel('localhost:50051')
    stub = recommendations_pb2_grpc.RecommendationServiceStub(channel)
    
    request = recommendations_pb2.RecommendationRequest(user_id=user_id, category=category, max_results=5)
    response = stub.Recommend(request)
    return response.recommendations


if __name__ == "__main__":
    recommendations = get_recommendations(1, recommendations_pb2.MYSTERY)
    print("Recommended books:", recommendations)
