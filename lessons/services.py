import stripe
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


print(create_stripe_payment(100, 'usd').id)
