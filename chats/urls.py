from django.urls import path
from .views import ChatView, ChatDeleteView, ChatUpdateView

urlpatterns = [
    path('chat/<int:pk>/edit/', ChatUpdateView.as_view(), name='chat_edit'),
    path('chat/<int:pk>/delete/', ChatDeleteView.as_view(), name='chat_delete'),
    path('chat/', ChatView.as_view(), name='chat'),
]
