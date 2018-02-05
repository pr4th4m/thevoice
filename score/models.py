from django.db import models
from django.conf import settings
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)

from performance.models import Performance


class Score(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    score = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(1)])

    def __str__(self):
        return "{0} scored by {1}".format(
            self.performance, self.mentor)
