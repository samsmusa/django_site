from re import template
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Subscriptions

from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import asyncio
import threading
from threading import Thread


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

class EmailThread(threading.Thread):
    def __init__(self, subject, template, title, content, image, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = render_to_string(template, {'wellcome_msg':title, 'content':content, 'image':image})
        self.text_content = strip_tags(self.html_content)
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMultiAlternatives(self.subject, self.text_content, 'samsmusa@outlook.com', self.recipient_list)
        msg.attach_alternative(self.html_content, "text/html")
        msg.send()

def send_html_mail(subject, template, title, content, image, recipient_list):
    EmailThread(subject, template, title, content, image, recipient_list).start()


def createSubscriber(sender, instance, created, **kwargs):
    if created:
        # user = instance
        # send_html_mail(
        #     subject='hello',
        #     template='email.html',
        #     title='world',
        #     content='content',
        #     image='https://images.unsplash.com/photo-1562585195-97aff4b3848c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
        #     recipient_list=[user]
        # )
        # html_content = render_to_string("email.html", {'wellcome_msg':'hello', 'content':'hello world', 'image':"https://images.unsplash.com/photo-1562585195-97aff4b3848c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80"})
        # text_content = strip_tags(html_content)
        # email = EmailMultiAlternatives(
        #     'Wellcome to scholarUni',
        #     text_content,
        #     'samsmusa@outlook.com',
        #     ['samsmusa.nstu@gmail.com']
        # )
        # email.attach_alternative(html_content, "text/html")
        # email.send()
        send_html_mail(subject='hi',
                    template='emailPersonal.html',
                    title='hello',
                    content='melo',
                    image='https://images.unsplash.com/photo-1562585195-97aff4b3848c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
                    recipient_list=[instance])

        print('send')

post_save.connect(createSubscriber,sender=Subscriptions)