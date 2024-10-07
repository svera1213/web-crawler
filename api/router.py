from django.urls import path, include
from .hacker_news.urls import hacker_news_urls

app_name = 'api'
urls = [
    path('hacker-news/', include(hacker_news_urls)),
]
