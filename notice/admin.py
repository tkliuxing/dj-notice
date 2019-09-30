from django.contrib import admin
from . import models

@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'create_time', 'last_modify', 'user')
    list_display_links = ('pk', 'title', 'create_time')

