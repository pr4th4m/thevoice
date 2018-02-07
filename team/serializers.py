from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Team,
    TeamCatalogue
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TeamCatalogueSerializer(serializers.ModelSerializer):
    mentor = UserSerializer()

    class Meta:
        model = TeamCatalogue
        fields = ('id', 'name', 'mentor')


class TeamSerializer(serializers.ModelSerializer):
    candidate = UserSerializer()
    team = TeamCatalogueSerializer()
    candidate_avg = serializers.IntegerField()

    class Meta:
        model = Team
        fields = ('id', 'candidate', 'team', 'candidate_avg')
