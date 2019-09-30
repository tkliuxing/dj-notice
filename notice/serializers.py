from . import models

from rest_framework import serializers


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Notice
        fields = (
            'pk',
            'title',
            'content',
            'create_time',
            'last_modify',
            'user'
        )
