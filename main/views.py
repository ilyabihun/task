from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from main.models import Ticket, Message
from main.serializer import UserSerializer, MessageSerializer, TicketSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == 'register':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(methods=['Post'], detail=False, url_path='register')
    def register(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first name')
        last_name = request.data.get('last name')
        email = request.data.get('email')
        us = User(username=username, first_name=first_name, last_name=last_name, email=email)
        us.set_password(password)
        us.save()
        refresh = RefreshToken.for_user(us)
        res_data = {
            'user': UserSerializer(us).data,
            'token': {
                'refresh': str(refresh),
                'acces': str(refresh.acces_token)
            }
        }
        return Response(res_data, status=status.HTTP_201_CREATED)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(creator=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        if self.request.user.is_staff and not self.request.user.is_superuser:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_staff and not self.request.user.is_superuser:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if self.request.user.is_staff and not self.request.user.is_superuser:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return super().update(request, *args, **kwargs)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(creator=self.request.user.id)
        return queryset
