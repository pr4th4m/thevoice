from rest_framework import viewsets
from django.db.models import Avg
import logging

from .serializers import TeamSerializer
from .models import Team


# Module logger
logger = logging.getLogger(__name__)


class TeamViewSet(viewsets.ModelViewSet):
    """
    """
    serializer_class = TeamSerializer

    def get_queryset(self):

        teams = Team.objects.select_related('team').order_by(
            '-team__name').annotate(
                candidate_avg=Avg('candidate__performance__score__score'))

        if not self.request.user.is_superuser:
            logger.debug("Fetching list of teams for non-admin users")
            teams = teams.filter(
                team__mentor=self.request.user)

        logger.debug("Fetched list of teams")
        return teams
