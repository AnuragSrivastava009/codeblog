"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="main"
urlpatterns = [
    path('', views.index,name='index'),
    path('about.html',views.about,name='about'),
    
    path('post.html',views.post,name='post'),
    path('contact',views.contacts,name="contact"),
  #  path('/index.html',views.index,name="index"),
    path('register.html',views.registers,name="register"),
    path('login.html',views.logins,name="login"),
    path('<my_slug>',views.my_slug, name='my_slug'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
