from multiprocessing import context
from django.http import request
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
import pandas as pd
from .models import Internship, Scholarships, SubscriberMessage, Subscriptions, UpdatedSchol, UpdatedIntern
from django.core.paginator import Paginator
from .forms import MessageForm, SubscriptionForm, EmailForm
from django.contrib import messages
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from itertools import chain
import random
from scraping.linkgen_intern import linkGenerationIntern 
from scraping.linkgen import linkGenerationScholarship 
from scraping import oppsql_intern
from scraping import oppsql


import threading
from threading import Thread
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailThread(threading.Thread):
    def __init__(self, subject, template, title, content, image, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = render_to_string(template, {'wellcome_msg':title, 'content':content, 'image':image})
        self.text_content = strip_tags(self.html_content)
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMultiAlternatives(self.subject, self.text_content, 'info@scholaruni.com', self.recipient_list)
        msg.attach_alternative(self.html_content, "text/html")
        msg.send()

def send_html_mail(subject, template, title, content, image, recipient_list):
    EmailThread(subject, template, title, content, image, recipient_list).start()
    

    

# subscription form validation 
def subsc(request,name=''):
    if request.method == "POST":
        forms = SubscriptionForm(request.POST)
        if forms.is_valid():
            forms.save(commit=True)

            messages.success(request, "Thanks for Connect with us!",extra_tags='success')
            if name:
                return redirect(name)
        else:
            messages.error(request,"Already Subscribe!",extra_tags='danger')




# Create your views here.
def about(request):
    return render(request,'scholarship/about.html')


def search(request):
    form = SubscriptionForm()
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    subsc(request)
    # result_list = list(chain(Scholarships.objects.filter(title__icontains=search_query), Internship.objects.filter(title__icontains=search_query)))
    internship = Internship.objects.filter(title__icontains=search_query)
    scholarship = Scholarships.objects.filter(title__icontains=search_query)
    # random.shuffle(internship)
    # random.shuffle(scholarship)
    context = {
        'internship':internship,
        'scholarship':scholarship,
        'form':form,
        "query":search_query

    }
    return render(request,'scholarship/search.html',context=context)

# home view 
def HomeView(request):
    form = SubscriptionForm()
    scholarship = Scholarships.objects.all()[:9]
    internship = Internship.objects.all()[:9]
    first_row_schol = scholarship[:3]
    first_row_intern = internship[:3]
    scholarship_row = scholarship[3:9]
    internship_row = internship[3:9]
    subsc(request,'contact')
    
    
    scholar_data = [
        {"countries":x.country, "Scholarship":1} if (x.country!='') else {"countries":'others', "Scholarship":1} for x in scholarship
    ]
    scholar_df = pd.DataFrame(scholar_data)
    scholar_df2 = scholar_df.groupby('countries').sum()
    scholar_df3 = scholar_df2.reset_index()
    schol_country = list(scholar_df3.countries)
    schol_data_value = list(scholar_df3.Scholarship)


    intern_data = [
        {"countries":x.country, "Internship":1} if (x.country!='') else {"countries":'others', "Internship":1} for x in internship
    ]
    intern_df = pd.DataFrame(intern_data)
    intern_df2 = intern_df.groupby('countries').sum()
    intern_df3 = intern_df2.reset_index()
    intern_country = list(intern_df3.countries)
    intern_data_value = list(intern_df3.Internship)

    context = {
        'first_row_schol':first_row_schol,
        'first_row_intern':first_row_intern,
        'scholarship_row':scholarship_row,
        'internship_row':internship_row,
        'form':form,
        'schol_country':schol_country,
        'schol_data':schol_data_value,
        'intern_country':intern_country,
        'intern_data':intern_data_value
    }
    return render(request,'scholarship/home.html',context=context)





def ScholarshipView(request):
    form = SubscriptionForm()
    scholarship = Scholarships.objects.all()
    paginator = Paginator(scholarship, 6)
    pageNumber  = request.GET.get('page')
    scholarship_row = paginator.get_page(pageNumber)
    
    subsc(request,'contact')


    context = {
        'scholarship_row':scholarship_row,
        'form':form
    }
    return render(request,'scholarship/scholarships.html',context=context)


def InternshipView(request):
    form = SubscriptionForm()
    internship = Internship.objects.all()
    paginator = Paginator(internship, 6)
    pageNumber  = request.GET.get('page')
    internship_row = paginator.get_page(pageNumber)
    
    subsc(request,'contact')


    context = {
        'internship_row':internship_row,
        'form':form
    }
    return render(request,'scholarship/internships.html',context=context)




    




# scholarship details view 
def ScholarshipDetailView(request,slug):
    scholarship = Scholarships.objects.get(slug=slug)
    form = SubscriptionForm()
    subsc(request)
    context = {
        'object':scholarship,
        'form':form
    }
    return render(request, 'scholarship/blog.html', context=context)
    

# inernship details view 
def InternshipDetailView(request,slug):
    internship = Internship.objects.get(slug=slug)
    form = SubscriptionForm()
    subsc(request)
    context = {
        'object':internship,
        'form':form
    }
    return render(request, 'scholarship/blog.html', context=context)
    


# contac us view 
def createMessage(request):
    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            message.save()

            messages.success(request, "Your message was sent")
            return redirect('home')
    context = {'form':form}
    return render(request, 'scholarship/contact.html', context=context)
    
    
    
@login_required(login_url='/admin')
def dashboard(request):
    # subscriptions = Subscriptions.objects.all()
    recpient = list(Subscriptions.objects.values_list('email', flat=True) )
    
    if request.method == 'POST':
        try:
            if list(request.POST.items())[1][0]=='title':
                form = EmailForm(request.POST)
                title = request.POST['title']
                subject = request.POST['subject']
                content = request.POST['body']
                print(title, subject, content)
                send_html_mail(
                    subject=subject,
                    template='emailPersonal.html',
                    title=title,
                    content=content,
                    image='https://images.unsplash.com/photo-1562585195-97aff4b3848c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
                    recipient_list=recpient
                )
        except:
            pass
        
        try:
            print(list(request.POST.items()))
            if list(request.POST.items())[1][0] == 'intern':
                print('intern')
                linkGenerationIntern()
                total = oppsql_intern.insertData()
                UpdatedIntern.objects.create(addPost=total) 
                
            if list(request.POST.items())[1][0] == 'schol':
                print('schol')
                linkGenerationScholarship()
                print(1)
                total = oppsql.insertDataScholarship()
                print(2)
                UpdatedSchol.objects.create(addPost=total) 
                print(3)
        except:
            pass
    form = EmailForm()
    subscriptions = Subscriptions.objects.all()
    updateInternPost = UpdatedIntern.objects.all()
    updateScholPost = UpdatedSchol.objects.all()
    context = {
        'updateInternPost':updateInternPost,
        'updateScholPost':updateScholPost,
        'subscriptions': subscriptions,
        'form':form,
    }
    return render(request, 'scholarship/dashboard.html', context=context)