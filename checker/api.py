from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from utils.cheapest_amount_calculator import find_cheapest_amount
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from rest_framework import status

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

CURRENCIES = ('usd', 'eur', 'gbp')


class ProviderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Provider class"""

    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer


class CheapestAmountViewSet(viewsets.ViewSet):

    def list(self, request):
        currency = request.GET['currency'].lower()
        if currency in CURRENCIES:
            if currency in cache:
                # get results from cache
                result = cache.get(currency)
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                result = find_cheapest_amount(currency)
                # store data in cache
                cache.set(currency, result, timeout=CACHE_TTL)
                return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response('Please choose the currency which exists:{}'.format(CURRENCIES),
                            status=status.HTTP_404_NOT_FOUND)
