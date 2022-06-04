from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Subscriptions

from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import asyncio

# message = "wellcome"

# async def saves():
#     print('presave')
#     asyncio.create_task(post_save1())
#     print('saved')

# async def post_save1():
#     print(4)
#     sum = 0
#     for i in range(100000):
#         sum += i
#     for i in range(100000):
#         sum += i
#     for i in range(1000000):
#         sum += i
        
#     return print(sum)
    

# @receiver(post_save, sender=Subscriptions)
# def createSubscriber(sender, instance, **kwargs):
#     # user = instance
#     # print('sending')
#     # html_content = render_to_string("email.html", {})
#     # text_content = strip_tags(html_content)
#     # email = EmailMultiAlternatives(
#     #     'Wellcome to scholarUni',
#     #     text_content,
#     #     'info@scholaruni.com',
#     #     ['samsmusa.nstu@gmail.com']
#     # )
#     # email.attach_alternative(html_content, "text/html")
#     # email.send()
#     # send_mail(
#     #     'WellCome Message',
#     #     message,
#     #     'info@scholaruni.com',
#     #     [user.email],
#     #     fail_silently=False

#     # )
#     print('send')
#     asyncio.run(saves())
#     print("send")

# post_save.connect(asyncio.run(saves()),sender=Subscriptions)