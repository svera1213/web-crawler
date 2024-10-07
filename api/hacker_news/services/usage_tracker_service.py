from api.models import UsageTracker
from api.models.usage_tracker import OrderingTypes

AVAILABLE_ORDERING_TYPES = [
    OrderingTypes.type_A, OrderingTypes.type_B
]


class UsageTrackerService(object):
    def __init__(self, request):
        self.request = request

    def track_usage(self):
        host = self.request.headers.get('HOST')
        ordering_type_param = self.request.query_params.get("ordering_type")
        ordering_type = ordering_type_param if ordering_type_param in AVAILABLE_ORDERING_TYPES else None
        UsageTracker(
            host=host,
            ordering_type=ordering_type
        ).save()
