"""helloscrapy URL Configuration

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
from cmdb import views          # import cmdb app 's views
from . import view

from django.views.generic.base import RedirectView


urlpatterns = [
    #url(r'^admin/', admin.site.urls),      #admin's  route
    url(r'^index/',views.index),
    #url(r'^$',view.hello)
    #url(r'^$',view.newhello)
    # favicon.cio
    url(r'^favicon\.ico$', RedirectView.as_view(url=r'static/images/favicon.ico'))
    
]

