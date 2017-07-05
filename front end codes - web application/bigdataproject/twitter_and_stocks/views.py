from django.shortcuts import render
from .models import Ibm, Tesla, United, Snap, American, Correlation
from django.template import loader
from django.views import generic

# Create your views here.
class ibmpage(generic.ListView):
    template_name = 'twitter_and_stocks/ibmpage.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Ibm.objects.all()


class teslapage(generic.ListView):
    template_name = 'twitter_and_stocks/teslapage.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Tesla.objects.all()


class unitedpage(generic.ListView):
    template_name = 'twitter_and_stocks/unitedpage.html'
    context_object_name = 'object'

    def get_queryset(self):
        return United.objects.all()


class snappage(generic.ListView):
    template_name = 'twitter_and_stocks/snappage.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Snap.objects.all()


class americanpage(generic.ListView):
    template_name = 'twitter_and_stocks/americanpage.html'
    context_object_name = 'object'

    def get_queryset(self):
        return American.objects.all()


class correlationpage(generic.ListView):
    template_name = 'twitter_and_stocks/correlation.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Correlation.objects.all()