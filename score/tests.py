from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ScoreTests(APITestCase):
    fixtures = ['user', 'performance', 'score']

    def setUp(self):
        url = reverse('login')
        data = {'username': 'seal.seal', 'password': 'thevoiceseal'}
        response = self.client.post(url, data, format='json')
        self.token = 'JWT {0}'.format(response.data['token'])

    def test_list_score_by_performance(self):
        url = reverse('scores-performance', args=[6])
        response = self.client.get(url, format='json',
                                   HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['score'], 67)
