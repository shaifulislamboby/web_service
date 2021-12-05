
from rest_framework.test import APITestCase
from .factories import FileDetailFactory
from django.urls import reverse
from rest_framework import status


class ApiTests(APITestCase):

    def setUp(self):
        self.client.credentials(HTTP_ACCEPT='application/json; version=1.0')
        self.one_random_line_endpoint = reverse('api_services:one_random_line')
        self.one_random_line_backward_endpoint = reverse('api_services:one_random_line_backwards')
        self.twenty_longest_line_endpoint = reverse('api_services:twenty_longest_lines')
        self.hundreds_longest_line_endpoint = reverse('api_services:hundreds_longest_lines')
        self.file_details = FileDetailFactory()
        self.one_random_line_response = self.client.get(self.one_random_line_endpoint)
        self.one_random_line_backward_response = self.client.get(self.one_random_line_backward_endpoint)
        self.twenty_longest_line_response = self.client.get(self.twenty_longest_line_endpoint)
        self.hundreds_longest_line_response = self.client.get(self.hundreds_longest_line_endpoint)

    def test_one_random_line_endpoint(self):
        """
        Ensure the endpoint is working properly.
        """

        self.assertEqual(self.one_random_line_response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.one_random_line_response.json()['file_name'], 'test__.txt')
        self.assertEqual(self.one_random_line_response.json()['line_number'], 11)
        self.assertEqual(self.one_random_line_response.json()['line_content'], 'Test is going on')
        self.assertEqual(self.one_random_line_response.json()['line_length'], 16)

    def test_one_random_line_backward_endpoint(self):
        """
        Ensure we are having the backward result properly.
        """
        self.assertEqual(self.one_random_line_backward_response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.one_random_line_backward_response.json()['random line backward'], 'on going is Test')

