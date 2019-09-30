from django.conf import settings
from django.db import models

class Notice(models.Model):
    title = models.CharField('标题', max_length=255, null=True, blank=True)
    content = models.TextField('内容', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modify = models.DateTimeField('发布时间', auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='创建者'
    )

    class Meta:
        verbose_name = '通知公告'
        verbose_name_plural = verbose_name
        ordering = ('-last_modify',)

    def __str__(self):
        return "{} {}".format(self.pk, self.title)
