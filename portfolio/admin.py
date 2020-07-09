from django.contrib import admin
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

# Register your models here.

admin.site.register(HomeModel)
admin.site.register(AboutModel)
admin.site.register(SkillModel)
admin.site.register(ServicesModel)
admin.site.register(HandelModel)
admin.site.register(PortfolioModel)
admin.site.register(PortfolioCategoryModel)
admin.site.register(ClientModel)
admin.site.register(TeamModel)
admin.site.register(CompamyBrandModel)
admin.site.register(BlogModel)
admin.site.register(ContactModel)
admin.site.register(FooterModel)


