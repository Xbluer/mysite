# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from books.models import Book

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        if request.GET['q']:
            q = request.GET['q']
            books = Book.objects.filter(title__icontains = q)
            return render_to_response('search_result.html', 
                                      {'books' : books, 'query': q})
        else:
            #message = 'You submitted an empty form.'
            return render_to_response('search_form.html',
                                      {'error': True})
    else:
        message = 'How did you get this page?'
    return HttpResponse(message)
