from rest_framework import filters

from common import WordCount


class HeadlineFilterA(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.annotate(
            word_count=WordCount('title')
        ).filter(word_count__gt=5).order_by('-comments')
