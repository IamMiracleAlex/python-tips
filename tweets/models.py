from django.db import models


class Link(models.Model):
    link = models.URLField(null=True)
    
class Tweet(models.Model):
    timestamp = models.DateTimeField()
    tip = models.TextField()
    links = models.ManyToManyField(Link)
    author = models.CharField(max_length=50)
    published = models.BooleanField(default=False)

