from rest_framework import permissions, viewsets, throttling
from scrapper.models import Headline
from ..serializers import HeadlineSerializer


class HeadlineViewSet(viewsets.ModelViewSet):
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer
    permissions_classes = [permissions.AllowAny]
    throttle_classes = [throttling.AnonRateThrottle]
