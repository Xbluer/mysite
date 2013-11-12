from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext, render
from django.core.mail import send_mail
from contact.forms import ContactForm

def contact(request):
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('email', 'noreplay@example.com'),
                    ['siteowner@example.com'],
                    )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
                initial = {'subject': 'I love your site!'})
#    return render_to_response('contact_form.html',
#                              {'form': form},
#                              context_instance = RequestContext(request))
    return render(request, 'contact_form.html', {'form': form})

def thanks(request):
    return render_to_response('thanks.html')
