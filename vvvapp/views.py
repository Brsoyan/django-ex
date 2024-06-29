from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import AddUser, Ping
from .serializers import AddUserSerializer, PingSerializer
from logger_util import ColoredLogger, Fore  # Import Fore from colorama for colors

logger = ColoredLogger(__name__)

class AddUserRequestViewSet(viewsets.ModelViewSet):
    queryset = AddUser.objects.all()
    serializer_class = AddUserSerializer

    def create(self, request, *args, **kwargs):
        ip = request.data.get('ip')
        existing_entry = AddUser.objects.filter(ip=ip).first()
        
        if existing_entry:
            serializer = self.get_serializer(existing_entry, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return super().create(request, *args, **kwargs)

class PingRequestViewSet(viewsets.ModelViewSet):
    queryset = Ping.objects.all()
    serializer_class = PingSerializer

    def create(self, request, *args, **kwargs):
        ip = request.data.get('ip')
        if not ip:
            return Response({'error': 'IP address is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = AddUser.objects.get(ip=ip)
            user.active = True
            user.save()
            logger.info(f'User updated {user.ip}.', color=Fore.GREEN)

            return super().create(request, *args, **kwargs)
        except AddUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        