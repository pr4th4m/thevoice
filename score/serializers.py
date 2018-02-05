from rest_framework import serializers

from .models import Score
from team.serializers import UserSerializer


class ScoreSerializer(serializers.ModelSerializer):
    mentor = UserSerializer()

    class Meta:
        model = Score
        fields = ('id', 'performance', 'mentor', 'score')
