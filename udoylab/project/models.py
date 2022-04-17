import uuid
from django.db import models
# from numpy import True_


def get_upload_path(instance, filename):
    model = instance.album.name
    return f'upload/{model}/{filename}'

class ImageAlbum(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255,null=False, blank=False)
    def __str__(self):
        return self.name 
    
class Image(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    image = models.ImageField(upload_to=get_upload_path)
    album = models.ForeignKey(ImageAlbum,null=True, blank=True, related_name='images', on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.id)
    
    
class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='default/')
    
    def __str__(self):
        return self.name 
    
class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    album = models.OneToOneField(ImageAlbum,null=True, blank=True, related_name='projectImage', on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    link = models.URLField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    
    def __str__(self):
        return self.title 
    
    

class BlogPost(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    album = models.OneToOneField(ImageAlbum, related_name='blogImage', on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title 
# Create your models here.



