from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
import logging

from .serializers import ScoreSerializer
from .models import Score

# Module logger
logger = logging.getLogger(__name__)


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

        logger.debug("Fetched scores for performance ID {0}".format(
            performance_id))
        return Response(serializer.data)
