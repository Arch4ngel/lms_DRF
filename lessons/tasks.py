import datetime

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail

from config import settings
from lessons.models import Course


@shared_task
def check_update(email):
    recipient_email = email
    for course in Course.objects.all():
        if course.date_update > course.date_publish:
            send_mail(
                subject='Информация о курсе',
                message=f'Курс был обновлен',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient_email]

            )
            course.date_publish = course.date_update
            course.save()


@shared_task
def check_activity():
    time_check = datetime.datetime.now()
    for user in User.objects.all():
        delta_login = time_check - user.last_login
        if delta_login > datetime.timedelta(days=30):
            user.is_active = False
            user.save()
