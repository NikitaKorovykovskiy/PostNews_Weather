# Create your tasks here
from datetime import date, time

from celery import shared_task
from constance import config
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Post


@shared_task
def send_email():
    # Получение настроек
    recipients = config.EMAIL_RECIPIENTS
    recipients = recipients.split()
    subject = config.EMAIL_SUBJECT
    message = config.EMAIL_TEXT
    today = date.today()
    # Получение новостей, опубликованных сегодня
    news = Post.objects.filter(pub_date__exact=today)
    context = {
        "message": message,
        "news": news,
    }
    # Генерация HTML-сообщения на основе шаблона и контекста
    email_message = render_to_string("news_email.html", context)
    # Отправка email
    send_mail(
        subject=subject,
        message="",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipients,
        html_message=email_message,
        fail_silently=False,
    )
