from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=200)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
