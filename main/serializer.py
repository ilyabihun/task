from django.contrib.auth.models import User

from rest_framework import serializers

from main.models import Message, Ticket


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'text',
            'ticket',
            'author',
            'created_at',
        ]


class TicketSerializer(serializers.ModelSerializer):
    message_for_ticket = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'id',
            'name',
            'creator',
            'created_at',
            'updated_at',
            'status',
            'ticket_message',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        ]
