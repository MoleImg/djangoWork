from django.shortcuts import render
import datetime

# Create your views here.

def hello(request):
    time_now = datetime.datetime.now()
    return render(request, 'hello.html', context=locals())
