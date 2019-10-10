from rest_framework import viewsets, permissions
from . import models
from . import serializers


class NoticeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Notice class"""

    queryset = models.Notice.objects.all()
    serializer_class = serializers.NoticeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
