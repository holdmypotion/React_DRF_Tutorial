from django.urls import path, include

from rest_framework import routers

from leads.api import LeadViewSet


router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'lead')

urlpatterns = [
    path('', include(router.urls)),
]