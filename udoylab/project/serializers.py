from dataclasses import fields
from pyexpat import model
from numpy import source
from rest_framework import serializers
from project.models import Project, Tag, BlogPost, ImageAlbum, Image


        

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
      
        

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
        
    # def get_image_url(self, obj):
    #     request = self.context.get("request")
    #     return request.build_absolute_uri(obj.image.url)
    

class ImageAlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = ImageAlbum
        fields = ['id','name','images']     
        
                
        
class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    album = ImageAlbumSerializer(many=False)
    class Meta:
        model = Project
        fields = '__all__'
        
        
        
class ImageAlbumSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = ImageAlbum
        fields = "__all__"