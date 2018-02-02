from django.db import models
from django.conf import settings


class Performance(models.Model):
    date = models.DateTimeField()
    song = models.CharField(max_length=140)
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)

    def __str__(self):
        return "{0} on {1}".format(self.song, self.date)
