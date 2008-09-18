from django.conf.urls.defaults import *
from models import Note


notes = Note.objects.all()

urlpatterns = patterns(
    '',
    (r'^$',
     'django.views.generic.list_detail.object_list',
     dict(queryset=notes)),
    (r'^note/(?P<slug>[-\w]+)/$', 
     'django.views.generic.list_detail.object_detail',
     dict(queryset=notes, slug_field='slug')),
    (r'^create/$','notes.views.create_note'),
    
)

