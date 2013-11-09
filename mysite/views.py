from django.http import HttpResponse, Http404
from django.template import Template, Context
import datetime

# for loader template
from django.template.loader import get_template

def hello(request):
    return HttpResponse("Hello world")

def current_datetime_1(request):
    now = datetime.datetime.now()
    t = Template('<html><head><title>time</title></head><body>It is now {{current}}.</body></html>')
    c = Context({"current": now})
    html = t.render(c)
    return HttpResponse(html)

def current_datetime_2(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    c = Context({"current": now})
    html = t.render(c)
    return HttpResponse(html)
