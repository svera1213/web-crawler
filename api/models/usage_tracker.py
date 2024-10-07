from django.db import models


class OrderingTypes:
    type_A = "A"
    type_B = "B"


ORDERING_TYPES = (
    (OrderingTypes.type_A, "Type A"),
    (OrderingTypes.type_B, "Type B"),
)


class UsageTracker(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=250, null=True)
    ordering_type = models.CharField(max_length=50, choices=ORDERING_TYPES, null=True)
