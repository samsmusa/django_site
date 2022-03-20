# from attr import field
from logging import PlaceHolder
from django.forms import ModelForm
from django import forms
from .models import Message, Subscriptions

class MessageForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control","PlaceHolder":"Your Name"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"form-control","PlaceHolder":"Your Email"
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control","PlaceHolder":"Enter Subject"
    }))
    body = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control","PlaceHolder":"Your Message"
    }))
    class Meta:
        model = Message
        fields = ['name', 'email','subject','body']

    # def __init__(self, *args, **kwargs):
    #     super(MessageForm,self).__init__(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({
    #             'class':'form-control'
    #         })

class SubscriptionForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"form-control","PlaceHolder":"Your Email"
    }))

    class Meta:
        model = Subscriptions
        fields = ['email']