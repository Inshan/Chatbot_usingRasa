from django.shortcuts import render
from django.http import JsonResponse
import requests

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        response = requests.post(RASA_URL, json={"sender": "user", "message": user_input})
        response_data = response.json()
        bot_response = response_data[0].get("text") if response_data else "I didn't understand that."
        return JsonResponse({"response": bot_response})
    return render(request, "chat.html")
