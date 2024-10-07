from rest_framework import routers
from .viewsets import HeadlineViewSet

router = routers.DefaultRouter()
router.register(r'headlines', viewset=HeadlineViewSet, basename='headlines')
hacker_news_urls = router.urls
