# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        if request.GET['q']:
            message = 'You searched for: %s' % request.GET['q']
        else:
            message = 'You submitted an empty form.'
    else:
        message = 'How did you get this page?'
    return HttpResponse(message)
