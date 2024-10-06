from django.db import models

from ..base_abstract_model import BaseAbstractModel


class Headline(BaseAbstractModel):
    news_id = models.CharField(max_length=150, unique=True)
    position = models.CharField(max_length=150, blank=True)
    title = models.CharField(max_length=150, blank=True)
    points = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

