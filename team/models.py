from django.db import models
from django.conf import settings


class TeamCatalogue(models.Model):
    name = models.CharField(max_length=42)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Team(models.Model):
    team = models.ForeignKey(TeamCatalogue, on_delete=models.CASCADE)
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)

    def __str__(self):
        return "{0} from {1}".format(self.candidate,
                                     self.team)
