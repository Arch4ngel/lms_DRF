from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='lessons/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='lessons/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    video_url = models.TextField(verbose_name='Ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    method_choice = [
        ('cash', 'наличными'),
        ('online', 'онлайн-перевод')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)
    transaction_id = models.TextField(verbose_name='Идентификатор платежа', **NULLABLE)
    dateime = models.DateTimeField(auto_now_add=True, verbose_name='Время платежа')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Урок', **NULLABLE)
    amount = models.IntegerField(verbose_name='Сумма')
    method = models.CharField(max_length=30, choices=method_choice, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.amount}'

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс', **NULLABLE)

    def __str__(self):
        return f'{self.is_active}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
