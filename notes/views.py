from django.utils import simplejson
from models import Note
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.contrib.auth.decorators import login_required


@login_required
def slug_available(request):
    if request.method == "GET":
        get = request.GET.copy()
        if get.has_key('slug'):
            slug_str = get['slug']
            if Note.objects.filter(slug=slug_str).count() == 0:
                return HttpResponse(slug_str)
            else:
                return HttpResponseServerError(slug_str)
    return HttpResponseServerError("Requires a slug field.")

@login_required
def create_note(request):
    error_msg = u"No POST data sent."
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('slug') and post.has_key('title'):
            slug = post['slug']
            if Note.objects.filter(slug=slug).count() > 0:
                error_msg = u"Slug already in use."
            else:
                title = post['title']
                new_note = Note.objects.create(title=title,slug=slug)
                return HttpResponseRedirect(new_note.get_absolute_url())
        else:
            error_msg = u"Insufficient POST data (need 'slug' and 'title'!)"
    return HttpResponseServerError(error_msg)

@login_required
def ajax_create_note(request):
    success = False
    to_return = {'msg':u'No POST data sent.' }
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('slug') and post.has_key('title'):
            slug = post['slug']
            if Note.objects.filter(slug=slug).count() > 0:
                to_return['msg'] = u"Slug '%s' already in use." % slug
            else:
                title = post['title']
                new_note = Note.objects.create(title=title,slug=slug)
                to_return['title'] = title
                to_return['slug'] = slug
                to_return['url'] = new_note.get_absolute_url()
                success = True
        else:
            to_return['msg'] = u"Requires both 'slug' and 'title'!"
    serialized = simplejson.dumps(to_return)
    if success == True:
        return HttpResponse(serialized, mimetype="application/json")
    else:
        return HttpResponseServerError(serialized, mimetype="application/json")

@login_required
def update_note(request, slug):
    if request.method == "POST":
        post = request.POST.copy()
        note = Note.objects.get(slug=slug)
        if post.has_key('slug'):
            slug_str = post['slug']
            if note.slug != slug_str:
                if Note.objects.filter(slug=slug_str).count() > 0:
                    error_msg = u"Slug already taken."
                    return HttpResponseServerError(error_msg)
                note.slug = slug_str
        if post.has_key('title'):
            note.title = post['title']
        if post.has_key('text'):
            note.text = post['text']
        note.save()
        return HttpResponseRedirect(note.get_absolute_url())
    error_msg = u"No POST data sent."
    return HttpResponseServerError(error_msg)

@login_required
def ajax_update_note(request, slug):
    success = False
    to_return = { 'msg': u"No POST data recieved." }
    if request.method == "POST":
        post = request.POST.copy()
        note = Note.objects.get(slug=slug)
        to_return['msg'] = "Updated successfully."
        success = True
        if post.has_key('slug'):
            slug_str = post['slug']
            if note.slug != slug_str:
                if Note.objects.filter(slug=slug_str).count() > 0:
                    to_return['msg'] = u"Slug '%s' already taken." % slug_str
                    to_return['slug'] = note.slug
                    success = False
                else:
                    note.slug = slug_str
                    to_return['url'] = note.get_absolute_url()
        if post.has_key('title'):
            note.title = post['title']
        if post.has_key('text'):
            note.text = post['text']
        note.save()
    print success
    print to_return
    print request.method
    serialized = simplejson.dumps(to_return)
    if success == True:
        return HttpResponse(serialized, mimetype="application/json")
    else:
        return HttpResponseServerError(serialized, mimetype="application/json")
