from django.urls import path
from . import  views

app_name='portfolio'


urlpatterns = [
    path('',views.index,name="IndexPage"),
    path('contact/',views.contact,name="ContactPage"),
    path('success/' , views.send_success , name='send_success'),
]

