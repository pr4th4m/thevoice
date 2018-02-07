from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.exceptions import PermissionDenied
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

        if not request.user.is_superuser:
            logger.debug("Fetching scores for non-admin user")
            queryset = queryset.filter(performance__team__team__mentor=request.user)

        serializer = self.serializer_class(queryset,
                                           context={'request': request},
                                           many=True)

        logger.debug("Fetched scores for performance ID {0}".format(
            performance_id))
        return Response(serializer.data)

    def get_queryset(self):

        queryset = Score.objects.select_related('performance').order_by('-score')

        if not self.request.user.is_superuser:
            logger.debug("Fetching scores for non-admin user")
            queryset = queryset.filter(
                performance__team__team__mentor=self.request.user)

        return queryset

    def get_object(self):

        if self.request.user.is_superuser:
            logger.debug("Fetching score for admin user")
            score = Score.objects.get(
                id=self.kwargs.get('pk'))
        else:
            try:
                logger.debug("Fetching score for non-admin user")
                score = Score.objects.get(id=self.kwargs.get('pk'),
                                        performance__team__team__mentor=self.request.user)
            except Exception as e:
                logger.error(e)
                raise PermissionDenied("Can't view scores for other members")

        return score
