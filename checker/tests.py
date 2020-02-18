from .models import Provider
from rest_framework.test import APITestCase, APIClient
from utils.test_endpoints import ApiUrl
from rest_framework import status

from .serializers import ProviderSerializer


class CreateProviderTest(APITestCase):
    """
    Tests for Create Provider
    """

    def setUp(self):
        self.provider = Provider.objects.create(
            name="Test Provider",
            url="http://www.google.com"
        )
        self.data = {'name': 'api test provider', 'url': 'https://github.com/alimetinozen'}

    def test_model_representation(self):
        self.assertEqual(str(self.provider), "Test Provider")

    def test_can_create_provider(self):
        response = self.client.post(path=ApiUrl.provider, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadProviderTest(APITestCase):
    """
    Tests for Read Provider
    """

    def setUp(self):
        self.provider = Provider.objects.create(
            name="Test Provider",
            url="http://www.google.com"
        )

    def test_can_read_provider_list(self):
        response = self.client.get(path=ApiUrl.provider)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateProviderTest(APITestCase):
    """
     Tests for Update Provider
    """

    def setUp(self):
        self.provider = Provider.objects.create(
            name="Test Provider",
            url="http://www.google.com"
        )
        self.data = ProviderSerializer(self.provider).data
        self.data.update({'name': 'Changed'})

    def test_can_update_provider(self):
        response = self.client.put(path=ApiUrl.provider + str(self.provider.pk) + "/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteProviderTest(APITestCase):
    """
    Tests for Delete Provider
    """

    def setUp(self):
        self.provider = Provider.objects.create(
            name="Test Provider",
            url="http://www.google.com"
        )

    def test_can_delete_provider(self):
        response = self.client.delete(ApiUrl.provider + str(self.provider.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CheapestAmountViewSetTest(APITestCase):
    def setUp(self):
        self.responses = [
            {
                "code": "usd",
                "rate": "4.14234"
            },
            {
                "code": "usd",
                "rate": "4.000"
            }]
        self.CURRENCIES = ('usd', 'eur', 'gbp')

    def test_find_cheapest_rate(self):
        min_rate = min(map(lambda resp: resp.get('rate'), self.responses))
        self.assertEqual(min_rate, self.responses[1].get("rate"))

    def test_currency(self):
        self.assertEqual('usd', self.CURRENCIES[0])

    def test_can_validate_endpoint(self):
        response = self.client.get(ApiUrl.amount + "?currency=aaa")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
