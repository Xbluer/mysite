from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.shortcuts import render_to_response
import datetime

# for loader template
from django.template.loader import get_template

def hello(request):
    return HttpResponse("Hello world")

def current_datetime_1(request):
    current = datetime.datetime.now()
    host_name = request.get_host()
    full_path = request.get_full_path()
    t = Template('''<html><head><title>time</title></head><body>It is now {{current}}.<br>
                    host: {{ host_name }}<br>
                    full_path: {{full_path}}<br>
                    </body></html>''')
    c = Context(locals())
    html = t.render(c)
    return HttpResponse(html)

def current_datetime_2(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    c = Context({"current": now})
    html = t.render(c)
    return HttpResponse(html)

def current_datetime_3(request):
    now = datetime.datetime.now()
    c = Context({"current": now})
    return render_to_response('current_datetime.html', c)

def current_datetime_4(request):
    current = datetime.datetime.now()
    return render_to_response('current_datetime_3.html', locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>', '\n'.join(html))

def display_meta_2(request):
    item_list = request.META.items()
    item_list.sort()
    c = Context({"item_list": item_list})
    return render_to_response('display_meta.html', c)
