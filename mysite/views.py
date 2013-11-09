from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")


