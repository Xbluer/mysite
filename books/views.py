# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from books.models import Book

def search(request):
    if 'q' in request.GET:
        if request.GET['q']:
            q = request.GET['q']
            books = Book.objects.filter(title__icontains = q)
            return render_to_response('search_result.html', 
                                      {'books' : books, 'query': q})
        else:
            return render_to_response('search_form.html',
                                      {'error': True})
    else:
        return render_to_response('search_form.html')
