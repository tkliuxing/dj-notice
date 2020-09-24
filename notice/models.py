from django.db import models


class Notice(models.Model):
    """通知公告,适用于全部公开的内容或部分公开的内容"""
    title = models.CharField('标题', max_length=255, null=True, blank=True, help_text='标题')
    content = models.TextField('内容', null=True, blank=True, help_text='内容')
    is_published = models.BooleanField('已发布', default=True, help_text='已发布')
    publish_date = models.DateField('发布日期', null=True, blank=True, help_text='发布日期')
    create_time = models.DateTimeField('创建时间', auto_now_add=True, help_text='创建时间')
    last_modify = models.DateTimeField('最后修改时间', auto_now=True, help_text='最后修改时间')
    create_user = models.ForeignKey(
        'usercenter.User', on_delete=models.SET_NULL, null=True, blank=True, db_constraint=False,
        related_name='my_notices', verbose_name='创建者ID', help_text='创建者ID'
    )
    is_public = models.BooleanField('全局公开', default=True, help_text='全局公开[false为部分公开，须填写public_user]')
    public_user = models.ManyToManyField(
        'usercenter.User', blank=True, related_name='own_notices', verbose_name='公开范围', help_text='公开范围'
    )

    class Meta:
        verbose_name = '01.通知公告'
        verbose_name_plural = verbose_name
        ordering = ('-publish_date', '-last_modify',)

    def __str__(self):
        return "{} {}".format(self.pk, self.title)

    @property
    def is_published_display(self):
        return '已发布' if self.is_published else '未发布'

    @property
    def publish_date_display(self):
        return self.publish_date.strftime('%Y-%m-%d') if self.publish_date else ''

    @property
    def last_modify_display(self):
        return self.last_modify.strftime('%Y-%m-%d')

    @property
    def create_time_display(self):
        return self.create_time.strftime('%Y-%m-%d')


class MailBox(models.Model):
    title = models.CharField('标题', max_length=255, null=True, blank=True, help_text='标题')
    content = models.TextField('内容', null=True, blank=True, help_text='内容')
    create_time = models.DateTimeField('创建时间', auto_now_add=True, help_text='创建时间')
    is_read = models.BooleanField('已读', default=False, help_text='已读')
    user = models.ForeignKey(
        'usercenter.User', on_delete=models.SET_NULL,
        null=True, blank=True, help_text='接收用户ID', db_constraint=False,
        related_name='+', verbose_name='接收用户'
    )
    from_user = models.ForeignKey(
        'usercenter.User', on_delete=models.SET_NULL,
        null=True, blank=True, help_text='发送用户ID', db_constraint=False,
        related_name='+', verbose_name='发送用户'
    )

    class Meta:
        verbose_name = '02.系统通知'
        verbose_name_plural = verbose_name
        ordering = ('-create_time', 'user_id',)

    def __str__(self):
        return "{} {}".format(self.pk, self.title)

    @classmethod
    def new_mail(cls, title, content, user, from_user=None):
        return cls.objects.create(
            title=title, content=content, user=user, from_user=from_user
        )
