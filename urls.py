from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns(
    '',
    # Devel Media Server                  
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),

    # Authentication Views
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    # Notes App
    (r'^', include('ajax_tut.notes.urls')),

)
