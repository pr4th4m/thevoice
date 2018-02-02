from rest_framework import viewsets

from .serializers import TeamSerializer
from .models import Team


class TeamViewSet(viewsets.ModelViewSet):
    """
    """
    serializer_class = TeamSerializer

    def get_queryset(self):

        teams = Team.objects.select_related('team').order_by(
            '-team__name')

        if not self.request.user.is_superuser:
            teams = teams.filter(
                team__mentor=self.request.user)

        return teams
