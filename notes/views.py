from models import Note
from django.http import HttpResponseRedirect, HttpResponseServerError

def create_note(request):
    error_msg = u"No POST data sent."
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('slug') and post.has_key('title'):
            title = post['title']
            slug = post['slug']
            new_note = Note.objects.create(title=title,slug=slug)
            return HttpResponseRedirect(new_note.get_absolute_url())
        error_msg = u"Insufficient POST data (need 'slug' and 'title'!)"
    return HttpResponseServerError(error_msg)
