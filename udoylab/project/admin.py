from django.contrib import admin
from .models import Project, BlogPost, Tag, Image, ImageAlbum

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','created','modified')
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','created','modified')
    
class TagAdmin(admin.ModelAdmin):
    list_display = (['name','image'])
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','image','album')

admin.site.register(ImageAlbum)
admin.site.register(Image,ImageAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(BlogPost ,BlogPostAdmin)
