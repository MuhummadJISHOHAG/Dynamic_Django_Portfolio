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

    # Home Section
    homeAll=HomeModel.objects.all()

    # About Section
    aboutAll=AboutModel.objects.get()

    # Skill Section
    skillAll=SkillModel.objects.all()

    # Service Section
    serviceAll=ServicesModel.objects.all()

    # Count Section
    handelAll=HandelModel.objects.all()

    # Portfolio Section
    portfolioAll=PortfolioModel.objects.all()
    portfolioCategoryAll=PortfolioCategoryModel.objects.all()

    # Client Section
    clientAll=ClientModel.objects.all()

    # Team Section
    teamAll=TeamModel.objects.all()

    # Brand Section
    brandAll=CompamyBrandModel.objects.all()

    # Blog Section
    blogAll=BlogModel.objects.all()

    
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
        'homeAll':homeAll,
        'aboutAll':aboutAll,
        'skillAll':skillAll,
        'serviceAll':serviceAll,
        'handelAll':handelAll,
        'portfolioAll':portfolioAll,
        'portfolioCategoryAll':portfolioCategoryAll,
        'clientAll':clientAll,
        'teamAll':teamAll,
        'brandAll':brandAll,
        'blogAll':blogAll,
        'form':form
    }
    return render(request,'index.html',content)


def send_success(request):
   return HttpResponse('thanks you for you email ^_^')
