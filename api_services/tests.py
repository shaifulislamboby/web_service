from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ApiTests(APITestCase):

    def setUp(self):
        self.calculator_endpoint = reverse('calculator-endpoint')
        self.expression_ = '?expression=1*(44*99)'
        self.expression__ = '?expression=3+33'
        self.calculator_response = self.client.get(self.calculator_endpoint +
                                                   self.expression_,
                                                   format='json')
        self.calculator_response_ = self.client.get(self.calculator_endpoint +
                                                    self.expression__,
                                                    format='json')

    def test_calculator_endpoint(self):
        """
        Ensure the endpoint is working properly.
        """
        self.assertEqual(self.calculator_response.status_code,
                         status.HTTP_200_OK)
        self.assertEqual(self.calculator_response.json()['expression'],
                         '1*(44*99)')
        self.assertEqual(self.calculator_response.json()['result'], 4356)

    def test_for_larger_expression(self):
        """
        Ensure we can have large expression with plus sign
        """

        self.assertEqual(self.calculator_response_.status_code,
                         status.HTTP_200_OK)
        self.assertEqual(self.calculator_response_.json()['expression'],
                         '3+33')
        self.assertEqual(self.calculator_response_.json()['result'], 36)
