from celery import shared_task
from django.core.mail import send_mail
from flower_shop.settings import EMAIL_HOST_USER


@shared_task
def send_mail_to_worker(user):
    send_mail(
        message="Регистрация прошла успешно!",
        from_email=EMAIL_HOST_USER,
        recipient_list=[user.email],
    )
