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
        NOTE: This isn't required for UI
        Get team for user/admin with candidate average
        """
        # TODO: Try to combine .get() and .annotate() together

        queryset = Team.objects.filter(
            id=self.kwargs.get('pk')).order_by(
                '-team__name').annotate(
                    candidate_avg=Avg('performance__score__score'))

        if not self.request.user.is_superuser:
            logger.debug("Fetching team for non-admin user")
            queryset = queryset.filter(team__mentor=self.request.user)

        if not queryset:
            raise PermissionDenied("Its not your team mate!")

        return queryset[0]
