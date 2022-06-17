from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Subscriptions
from django.conf import settings
from django.core.mail import send_mail

message = "wellcome"

def createSubscriber(sender, instance, created, **kwargs):
    if created:
        user = instance
        html_content = render_to_string("email.html", {})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            'Wellcome to scholarUni',
            text_content,
            'info@scholaruni.com',
            [user.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()

post_save.connect(createSubscriber,sender=Subscriptions)