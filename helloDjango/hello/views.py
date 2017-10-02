from django.shortcuts import render
import datetime

# Create your views here.

def hello(request, time_set):
    print(time_set)
    time_now = datetime.datetime.now()
    return render(request, 'hello.html', context=locals())
