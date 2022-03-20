from django.contrib import admin

# Register your models here.
from .models import Internship, Scholarships, Message, Subscriptions

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','is_read')
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email','created')
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('title','country','publisher','add_date')
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('title','country','publisher','add_date')

admin.site.register(Scholarships,ScholarshipAdmin)
admin.site.register(Internship,InternshipAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Subscriptions,SubscriptionAdmin)