from rest_framework.decorators import api_view
from rest_framework.response import Response
from .inference import get_chatbot_response

@api_view(["POST"])
def chatbot_response(request):
    user_input = request.data.get("query", "")
    if not user_input:
        return Response({"error": "Query not provided."}, status=400)

    result = get_chatbot_response(user_input)
    return Response({
        "query": user_input,
        "intent": result["label"],
        "confidence": round(result["score"], 4)
    })
