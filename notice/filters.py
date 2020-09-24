import django_filters

from . import models


class NoticeFilterSet(django_filters.FilterSet):

    class Meta:
        model = models.Notice
        fields = (
            'is_published',
            'public_user',
        )
