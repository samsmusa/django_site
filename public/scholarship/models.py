from distutils.command.upload import upload
import email
from enum import auto
from statistics import mode
from typing import Tuple
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
import uuid 

# Create your models here.

class Scholarships(models.Model):
    # id = models.IntegerField(auto_created=True, unique=True, primary_key=True, editable= False)
    feature_image = models.ImageField(null=True,blank=True,default="default/default.png",upload_to="uploads/scholarship/")
    slug = models.SlugField(null=True,unique=True)
    publisher = models.CharField(max_length=200,null=True,blank=True)
    title = models.CharField(max_length=500,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    star = models.IntegerField(null=True,blank=True)
    post_content = RichTextField(null=True,blank=True)
    publish_date = models.CharField(max_length=100,null=True,blank=True)
    add_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("scholar_blog", kwargs={"slug": self.slug})

    

    class Meta:
        ordering = ['-add_date']



class Internship(models.Model):
    # id = models.IntegerField(auto_created=True, unique=True, primary_key=True, editable= False)
    feature_image = models.ImageField(null=True,blank=True,default="default/default.png",upload_to="uploads/internship/")
    slug = models.SlugField(null=True,unique=True)
    publisher = models.CharField(max_length=200,null=True,blank=True)
    title = models.CharField(max_length=500,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    star = models.IntegerField(null=True,blank=True)
    post_content = RichTextField(null=True,blank=True)
    publish_date = models.CharField(max_length=100,null=True,blank=True)
    add_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("intern_blog", kwargs={"slug": self.slug})
    

    class Meta:
        ordering = ['-add_date']
    

class Message(models.Model):
    name = models.CharField(max_length=200,null=True,blank=False)
    email = models.EmailField(max_length=200,null=True,blank=False)
    subject = models.CharField(max_length=200,null=True,blank=False)
    body = models.TextField()
    is_read = models.BooleanField(default=False,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.subject 

    class Meta:
        ordering = ['is_read','created']

class SubscriberMessage(models.Model):
    subject = models.CharField(max_length=200,null=True,blank=False)
    body = RichTextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.subject 

    class Meta:
        ordering = ['created']



class Subscriptions(models.Model):
    
    email = models.EmailField(max_length=200,null=True,blank=False,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.email 

    class Meta:
        ordering = ['created']
        
        

class UpdatedIntern(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    addPost = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.created
    
    class Meta:
        ordering = ['created']
        
        
class UpdatedSchol(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    addPost = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.created
    
    class Meta:
        ordering = ['created']
