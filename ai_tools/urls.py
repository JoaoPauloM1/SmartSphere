from django.urls import path
from ai_tools.views import index, chatbot_view

urlpatterns = [
    path('', index, name='index'),
    path('chatbot/', chatbot_view, name='chatbot'), 
]