from rest_framework import serializers

from .models import Performance
from team.serializers import UserSerializer


class PerformanceSerializer(serializers.ModelSerializer):
    candidate = UserSerializer()

    class Meta:
        model = Performance
        fields = ('id', 'date', 'song', 'candidate')
