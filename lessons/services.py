import stripe
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from stripe import InvalidRequestError
from config import settings


def create_stripe_payment(amount, currency):
    stripe.api_key = settings.STRIPE_API_KEY
    response = stripe.PaymentIntent.create(
      amount=amount,
      currency=currency
    )
    return response


def retrieve_stripe_payment(payment_id):
    try:
        stripe.api_key = settings.STRIPE_API_KEY
        response = stripe.PaymentIntent.retrieve(payment_id)
        return response
    except stripe.error.InvalidRequestError:
        raise InvalidRequestError("Платеж не найден")


def create_periodic_activity_check():
    schedule, created = IntervalSchedule.objects.get_or_create(
         every=3,
         period=IntervalSchedule.DAYS,
     )

    PeriodicTask.objects.create(
         interval=schedule,
         name='Activity check',
         task='lessons.tasks.check_activity',)
