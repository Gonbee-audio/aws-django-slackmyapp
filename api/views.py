from django.shortcuts import render
from slack.models import ChatMessage
from rest_framework import viewsets, filters
from .serializers import ChatMessageSerializer


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all() 
    serializer_class = ChatMessageSerializer
