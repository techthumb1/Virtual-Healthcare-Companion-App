from django.contrib import admin
from django.urls import path, include
from app.views import user_view, device_view, health_insight_view, health_goal_view, appointment_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/user/', user_view.UserAPIView.as_view(), name='user'),
    path('api/devices/', device_view.HealthDeviceListCreateView.as_view(), name='devices'),
    path('api/insights/', health_insight_view.HealthInsightListView.as_view(), name='insights'),
    path('api/goals/', health_goal_view.HealthGoalListCreateView.as_view(), name='goals'),
    path('api/appointments/', appointment_view.AppointmentListCreateView.as_view(), name='appointments'),
]
