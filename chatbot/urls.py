from django.urls import path
from .views import chat, chatbot_page

urlpatterns = [
    path('chat/', chat, name='chat'),
    path('', chatbot_page, name='chatbot_page'),
    
]