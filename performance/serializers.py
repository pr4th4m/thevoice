from rest_framework import serializers

from .models import Performance


class PerformanceSerializer(serializers.ModelSerializer):
    performance_avg = serializers.IntegerField()

    class Meta:
        model = Performance
        fields = ('id', 'date', 'song', 'performance_avg')
