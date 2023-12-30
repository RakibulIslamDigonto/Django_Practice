# from django.conf.urls import url
from django.urls import path
from FirstApp import views

urlpatterns = [
    path('', views.index, name='index')
    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about')
]


