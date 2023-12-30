from django.contrib import admin
from django.urls import path
from FirstApp import views
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FirstApp.urls')),
    # path('', views.index, name='index'),
    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about'),
]
