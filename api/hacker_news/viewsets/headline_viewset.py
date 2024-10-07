from rest_framework import permissions, viewsets, throttling
from rest_framework.response import Response
from scrapper.models import Headline
from ..serializers import HeadlineSerializer
from ..filters import HeadlineFilterA, HeadlineFilterB


class HeadlineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer
    permissions_classes = [permissions.AllowAny]
    throttle_classes = [throttling.AnonRateThrottle]

    def filter_queryset(self, queryset):
        ordering_type = self.request.query_params.get("ordering_type", "default")
        if ordering_type == "A":
            return HeadlineFilterA().filter_queryset(self.request, queryset, self)
        elif ordering_type == "B":
            return HeadlineFilterB().filter_queryset(self.request, queryset, self)
        else:
            pass
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
