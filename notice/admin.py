from django.contrib import admin
from . import models


@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'create_time', 'last_modify')
    list_display_links = ('pk', 'title', 'create_time')


@admin.register(models.MailBox)
class MailBoxAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'from_user', 'title', 'create_time', 'is_read')
    list_display_links = ('pk', 'user', 'from_user', 'title', 'create_time')
