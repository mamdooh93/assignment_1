"""Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include

from blog.views import *
from todo.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
  #  url(r'^(?P<entry>[0-9]+)', get_example1),
    url(r'^blog/entries/$', show_example1),
    url(r'^$', show_todo),
    url(r'^(?P<todo_id>[0-9]+)', get_todo),
#   url(r'^blog/entries(?P<todo_id>[0-9]+)', get_example1())




]

