from django.db import models


class BaseAbstractModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=True)

    class Meta:
        abstract = True
