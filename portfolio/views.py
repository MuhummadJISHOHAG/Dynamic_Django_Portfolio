from django.shortcuts import render
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
        'blogAll':blogAll,

    }
    return render(request,'index.html',content)
