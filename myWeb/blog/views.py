from django.shortcuts import render, render_to_response
from django.template import RequestContext
import datetime

# Create your views here.
def home_page(request):
    time_now = datetime.datetime.now()
    return render(request, 'home.html', context=locals())
