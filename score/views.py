from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from .serializers import ScoreSerializer
from .models import Score


class ScoreViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    @list_route(url_name='performance', url_path='performance/(?P<performance_id>[0-9]+)')
    def get_by_performance(self, request, performance_id=None):

        queryset = Score.objects.select_related('performance').filter(
            performance=performance_id).order_by('-score')

        serializer = self.serializer_class(queryset,
                                           context={'request': request},
                                           many=True)
        return Response(serializer.data)
