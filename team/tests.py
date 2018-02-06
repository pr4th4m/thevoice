from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TeamTests(APITestCase):
    fixtures = ['user', 'team_catalogue', 'team']

    def setUp(self):
        url = reverse('login')
        data = {'username': 'seal.seal', 'password': 'thevoiceseal'}
        response = self.client.post(url, data, format='json')
        self.token = 'JWT {0}'.format(response.data['token'])

    def test_list_teams(self):
        url = reverse('teams-list')
        response = self.client.get(url, format='json',
                                   HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['team']['name'], 'Team Seal S6')
