from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return u"Note(%s,%s)" % (self.title, self.slug)

    def get_absolute_url(self):
        return u"/note/%s/" % self.slug
