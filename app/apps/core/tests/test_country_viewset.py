from rest_framework import status

from app.utils.testing import BaseTestCase

from ..factories import CountryFactory


class CountryViewTests(BaseTestCase):
    def setUp(self):
        self.list_url = "/api/countries/"
        self.retrieve_url = "/api/countries/1/"
        self.countries = CountryFactory.create_batch(40)

    def test_list_request(self):
        """Ensure authorized users can list all objects"""
        url = self.list_url
        response = self.client.get(url)
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data["results"]), len(self.countries))

    def test_create_request(self):
        """Ensure authorized/unauthorized users cannot create new object"""
        url = self.list_url
        payload = {}
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_request(self):
        """Ensure authorized/unauthorized users cannot update single object"""
        url = self.retrieve_url
        payload = {}
        response = self.client.put(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update_request(self):
        """Ensure authorized/unauthorized users cannot update single object partially"""
        url = self.retrieve_url
        payload = {}
        response = self.client.patch(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_request(self):
        """Ensure authorized/unauthorized users cannot retrieve single object"""
        url = self.retrieve_url
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_destroy_request(self):
        """Ensure authorized/unauthorized users cannot destroy single object"""
        url = self.retrieve_url
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
