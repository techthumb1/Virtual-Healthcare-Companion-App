from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import HealthGoal
from .serializers import HealthGoalSerializer

class HealthGoalListCreateView(generics.ListCreateAPIView):
    serializer_class = HealthGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HealthGoal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
