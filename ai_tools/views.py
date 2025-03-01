from django.shortcuts import render
from ai_tools.services.chatbot import chatbot

def index(request):
    return render(request, 'index.html')

def chatbot_view(request):
    return render(request, 'chatbot.html')