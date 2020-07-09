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

    content={
        'homeAll':homeAll,
        'aboutAll':aboutAll,
        'skillAll':skillAll,
        'serviceAll':serviceAll
    }
    return render(request,'index.html',content)
