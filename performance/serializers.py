from rest_framework import serializers

from .models import Performance
from team.serializers import UserSerializer


class PerformanceSerializer(serializers.ModelSerializer):
    candidate = UserSerializer()
    performance_avg = serializers.IntegerField()

    class Meta:
        model = Performance
        fields = ('id', 'date', 'song',
                  'candidate', 'performance_avg')
