from . import models

from rest_framework import serializers
from usercenter.serializers import UserMinSerializer


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Notice
        fields = (
            'pk',
            'title',
            'content',
            'is_published',
            'is_published_display',
            'publish_date',
            'publish_date_display',
            'create_time',
            'create_time_display',
            'last_modify',
            'last_modify_display',
            'create_user',
            'is_public',
            'public_user',
        )


class MailBoxSerializer(serializers.ModelSerializer):
    user_info = UserMinSerializer(read_only=True, source='user')
    from_user_info = UserMinSerializer(read_only=True, source='from_user')

    class Meta:
        model = models.MailBox
        fields = (
            'pk',
            'title',
            'content',
            'create_time',
            'is_read',
            'user',
            'user_info',
            'from_user',
            'from_user_info',
        )


class MailBoxUnreadSerializer(serializers.Serializer):
    count = serializers.IntegerField(label='未读消息数量', read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
