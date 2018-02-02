from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from .serializers import PerformanceSerializer
from .models import Performance


class PerformanceViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

    @list_route(url_name='candidate', url_path='candidate/(?P<candidate_id>[0-9]+)')
    def get_by_candidate(self, request, candidate_id=None):

        queryset = Performance.objects.select_related('candidate').filter(
            candidate=candidate_id).order_by('-date')

        serializer = self.serializer_class(queryset,
                                           context={'request': request},
                                           many=True)
        return Response(serializer.data)
