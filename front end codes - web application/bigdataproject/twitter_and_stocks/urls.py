"""bigdataproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from .import views

app_name = 'twitter_and_stocks'

urlpatterns = [
    url(r'^ibm/$', views.ibmpage.as_view(), name="ibmpage"),
    url(r'^tesla/$', views.teslapage.as_view(), name="teslapage"),
    url(r'^united/$', views.unitedpage.as_view(), name="unitedpage"),
    url(r'^snap/$', views.snappage.as_view(), name="snappage"),
    url(r'^american/$', views.americanpage.as_view(), name="americanpage"),
    url(r'^correlation/$', views.correlationpage.as_view(), name="correlationpage"),

]
