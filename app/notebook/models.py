from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User


def post_time():
    return datetime.now() + timedelta(days=1)


class Notebook(models.Model):
    ACTIVITY_STATUS = (
        (0, 'Активно'),
        (1, 'Отложено'),
        (2, 'Выполнено'),
    )

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default='', blank=True, verbose_name='Текст')
    date_add = models.DateTimeField(default=post_time, verbose_name='Время создания')
    important = models.BooleanField(default=False, verbose_name='Важная запись')
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT, editable=False)
    activity = models.IntegerField(default=0, choices=ACTIVITY_STATUS, verbose_name='Статус задачи')

    def __str__(self):
        return self.title
