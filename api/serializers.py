from rest_framework import serializers
from django import forms
from slack.models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ('username','text','image', 'good')
    