from django.conf import settings
from django.core.mail import send_mail

from flower_shop.celery import app


@app.task()
def send_order(email: str, id: str,):
    message = f'Ваш заказ #{id} получен и обрабатывается администратором, ждите обратной связи)) \n'
    send_mail(
        "FlowerShop",
        message, settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )
    return 'Send email send order'
