# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response

from books.models import Book

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter an search term.')
        elif len(q) > 20:
            errors.append('It\'too long.')
        else: 
            books = Book.objects.filter(title__icontains = q)
            return render_to_response('search_result.html', 
                                      {'books' : books, 'query': q})
    return render_to_response('search_form.html', {'errors':errors})
