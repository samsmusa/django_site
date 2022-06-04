from django.contrib import admin

# Register your models here.
from .models import Internship, Scholarships, Message, Subscriptions, Tags, UpdatedIntern, UpdatedSchol, Blog, BlogTag

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','is_read')
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email','created')
class UpdatedInternAdmin(admin.ModelAdmin):
    list_display = ('addPost','created')
class UpdatedScholnAdmin(admin.ModelAdmin):
    list_display = ('addPost','created')
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('title','country','publisher','add_date')
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('title','country','publisher','add_date')
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','created')

admin.site.register(Scholarships,ScholarshipAdmin)
admin.site.register(Internship,InternshipAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Subscriptions,SubscriptionAdmin)  
admin.site.register(UpdatedIntern,UpdatedInternAdmin)  
admin.site.register(UpdatedSchol,UpdatedScholnAdmin)  
admin.site.register(Blog,BlogAdmin)  
admin.site.register(Tags)  
admin.site.register(BlogTag)  