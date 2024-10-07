from rest_framework import filters

from common import WordCount


class HeadlineFilterB(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.annotate(
            word_count=WordCount('title')
        ).filter(word_count__lte=5).order_by('-points')
