from rest_framework import serializers
from scrapper.models import Headline


class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = [
            'id',
            'news_id',
            'position',
            'title',
            'points',
            'comments',
        ]
