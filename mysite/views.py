from django.http import HttpResponse, Http404
from django.template import Template, Context
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime_1(request):
    now = datetime.datetime.now()
    t = Template('<html><head><title>time</title></head><body>It is now {{current}}.</body></html>')
    c = Context({"current": now})
    html = t.render(c)
    return HttpResponse(html)
