from django.shortcuts import render
from django.http import HttpResponse
import datetime


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def send_datetime(request):
    # delay by 1000 ms
    return HttpResponse(str(datetime.datetime.now()))
