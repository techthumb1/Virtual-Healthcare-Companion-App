from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import HealthInsight
from .serializers import HealthInsightSerializer

class HealthInsightListView(generics.ListAPIView):
    serializer_class = HealthInsightSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HealthInsight.objects.filter(user=self.request.user)
