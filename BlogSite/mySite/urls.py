"""mySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from see import views as see

urlpatterns = [
    url(r'^$',see.home),url(r'^home/$',see.home),#首页样式
    url(r'^asuradong/', admin.site.urls),#官方已经规定了amdin格式，不需要$限制了
    url(r'^blog/$',see.blog),url(r'contact/$',see.contact),url(r'about/$',see.about),url(r'more/$',see.more),
]
