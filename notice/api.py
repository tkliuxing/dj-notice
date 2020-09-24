from rest_framework import viewsets, permissions
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.response import Response
from django.db.models import Q

from . import models
from . import serializers
from . import filters


class NoticeViewSet(viewsets.ModelViewSet):
    """通知公告API"""

    queryset = models.Notice.objects.all()
    serializer_class = serializers.NoticeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.NoticeFilterSet


class ViewMyNoticeViewSet(viewsets.ReadOnlyModelViewSet):
    """登录用户查看通知公告API"""

    queryset = models.Notice.objects.all()
    serializer_class = serializers.NoticeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.NoticeFilterSet

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_anonymous:
            return qs.none()
        return qs.filter(
            Q(is_public=True) | Q(public_user=self.request.user)
        )


class MailBoxViewSet(viewsets.ModelViewSet):
    """用户系统消息API"""
    queryset = models.MailBox.objects.all()
    serializer_class = serializers.MailBoxSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('user_id', 'is_read',)


class MailBoxUnreadCountView(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    """用户未读系统消息数API"""
    queryset = models.MailBox.objects.all()
    serializer_class = serializers.MailBoxUnreadSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def list(self, request, *args, **kwargs):
        count = models.MailBox.objects.filter(user_id=request.user.pk, is_read=False).count()
        return Response(self.serializer_class({'count': count}).data)


class MailBoxMarkAllReadView(viewsets.GenericViewSet):
    """标记所有消息为已读"""
    queryset = models.MailBox.objects.all()
    serializer_class = serializers.MailBoxSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def create(self, request, *args, **kwargs):
        qs = models.MailBox.objects.filter(user_id=request.user.pk, is_read=False)
        qs.update(is_read=True)
        return Response(self.serializer_class(qs, many=True).data)
