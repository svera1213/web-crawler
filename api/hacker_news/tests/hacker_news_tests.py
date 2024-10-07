from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode


class HackerNewsTests(TestCase):
    def test_list_endpoint_exists(self):
        url = reverse('api:headlines-list')
        response = self.client.head(url)
        self.assertTrue(response.status_code is not None)

    def test_detail_endpoint_exists(self):
        url = reverse('api:headlines-detail', kwargs={"pk": 0})
        response = self.client.head(url)
        self.assertTrue(response.status_code is not None)

    def test_list_endpoint_accept_query_params(self):
        url = reverse('api:headlines-list')
        query_kwargs = {"ordering_type": 'A'}
        response = self.client.head(f'{url}?{urlencode(query_kwargs)}')
        self.assertTrue(response.status_code is not None)
