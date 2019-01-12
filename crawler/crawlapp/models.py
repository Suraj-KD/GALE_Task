from django.db import models

# Create your models here.
class Crawl(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True)


class Url(models.Model):
    url = models.CharField(max_length=3000, null=True, blank=True)
    crawl = models.ForeignKey(Crawl, related_name='urls', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', null=True, on_delete=models.Empty)
    depth = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    visited = models.DateTimeField(null=True)
    content_type = models.CharField(max_length=128, null=True)
