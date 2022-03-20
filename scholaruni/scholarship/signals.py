from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Subscriptions

from django.conf import settings
from django.core.mail import send_mail

message = "wellcome"

def createSubscriber(sender, instance, created, **kwargs):
    if created:
        user = instance
        send_mail(
            'WellCome Message',
            message,
            settings.EMAIL_HOST,
            [user.email],
            fail_silently=False

        )

post_save.connect(createSubscriber,sender=Subscriptions)