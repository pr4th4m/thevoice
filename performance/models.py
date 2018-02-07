from django.db import models

from team.models import Team


class Performance(models.Model):
    date = models.DateTimeField()
    song = models.CharField(max_length=140)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} on {1}".format(self.song, self.date)
