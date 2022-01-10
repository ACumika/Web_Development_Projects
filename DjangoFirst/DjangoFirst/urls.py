"""DjangoFirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstapp import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='home'),
    path('create/',views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    re_path(r'^about/',TemplateView.as_view(template_name="about.html",extra_context={"header": "О сайте"})),
    re_path(r'^contact/', TemplateView.as_view(template_name="contact.html")),
    re_path(r'^products/$', views.products),
    re_path(r'products/(?P<product>\d+)/',views.products),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+/)',views.users),
    path('details/', views.details)
    #path('products/', views.products),
    #path('products/<int:productid>/', views.products),
    #path('users/', views.users),
    #path('users/<int:id>/<name>/', views.users),
    #path('admin/', admin.site.urls),
]
