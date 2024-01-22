from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='lessons/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='lessons/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    video_url = models.TextField(verbose_name='Ссылка на видео')
