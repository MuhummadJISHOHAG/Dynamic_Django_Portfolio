from django.shortcuts import render,redirect
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect

from .models import (
    HomeModel,
    AboutModel,
    SkillModel,
    ServicesModel,
    HandelModel,
    PortfolioModel,
    PortfolioCategoryModel,
    ClientModel,
    TeamModel,
    CompamyBrandModel,
    BlogModel,
    ContactModel,
    FooterModel
)
from .forms import ContactForms
# Create your views here.

def index(request):
    homeAll=HomeModel.objects.all()
    aboutAll=AboutModel.objects.get()
    skillAll=SkillModel.objects.all()
    serviceAll=ServicesModel.objects.all()
    handelAll=HandelModel.objects.all()
    clientAll=ClientModel.objects.all()
    teamAll=TeamModel.objects.all()
    brandAll=CompamyBrandModel.objects.all()
    blogAll=BlogModel.objects.all()

    content={
        'homeAll':homeAll,
        'aboutAll':aboutAll,
        'skillAll':skillAll,
        'serviceAll':serviceAll,
        'handelAll':handelAll,
        'clientAll':clientAll,
        'teamAll':teamAll,
        'brandAll':brandAll,
        'blogAll':blogAll
    }
    return render(request,'index.html',content)


def contact(request):

    if request.method=='POST':
        form=ContactForms(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            selectOption=form.cleaned_data['selectOption']
            message=form.cleaned_data['message']
            recipients=['admin@example.com']

            try:
                if name:
                    recipients.append(email)
                send_mail(email,selectOption,message,recipients)
            except BadHeaderError:
                return HttpResponse('Invalid Header')

            return redirect('portfolio:send_success')

    else:
        form=ContactForms()
        
    content={
        'form':form
    }

    return render(request,'contact.html',content)

def send_success(request):
   return HttpResponse('thanks you for you email ^_^')
