from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.core.mail import send_mail

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject')
        if not request.POST.get('message', ''):
            errors.append('Enter a message')
        if not request.POST.get('email') or '@' not in request.POST['email']:
            errors.append('Enter your email address')
        if not errors:
            send_mail(
                    request.POST['subject'],
                    request.POST['message'],
                    #not request.POST['email'],
                    request.POST.get('email', 'noreply@example.com'),
                    # replace ['sitowner@example.com']
                    [''],
                    )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html', {'errors': errors},
                              context_instance = RequestContext(request))

def thanks(request):
    return render_to_response('thanks.html')
