from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
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
        """
        List teams for user/admin with candidate average
        """

        teams = Team.objects.select_related('team').order_by(
            '-team__name').annotate(
                candidate_avg=Avg('performance__score__score'))

        if not self.request.user.is_superuser:
            logger.debug("Fetching list of teams for non-admin users")
            teams = teams.filter(
                team__mentor=self.request.user)

        logger.debug("Fetched list of teams")
        return teams

    def get_object(self):
        """
        Get team for user/admin with candidate average
        """

        if self.request.user.is_superuser:
            logger.debug("Fetching team for admin user")
            team = Team.objects.get(
                id=self.kwargs.get('pk'))
        else:
            try:
                logger.debug("Fetching team for non-admin user")
                team = Team.objects.get(id=self.kwargs.get('pk'),
                                        team__mentor=self.request.user)
            except Exception as e:
                logger.error(e)
                raise PermissionDenied("Its not your team mate!")

        return team
