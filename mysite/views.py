from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><head><title>time</title></head><body>It is new %s.</body></html>" % now
    return HttpResponse(html)
