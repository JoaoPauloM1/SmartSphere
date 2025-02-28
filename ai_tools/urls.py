from django.urls import path
from ai_tools.views import index

urlpatterns = [
    path('', index) 
]