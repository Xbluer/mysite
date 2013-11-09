from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#from mysite.views import hello, current_datetime, hours_ahead
from mysite.views import hello, current_datetime_1, current_datetime_2, current_datetime_3, \
    current_datetime_4

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^time1/$', current_datetime_1),
    ('^time2/$', current_datetime_2),
    ('^time3/$', current_datetime_3),
    ('^time4/$', current_datetime_4),
    #(r'^time/plus/(\d{1,2})/$', hours_ahead),
    ('^$', current_datetime_1),     # homepage
)
