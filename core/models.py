from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.title, self.body)
