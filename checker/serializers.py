from . import models

from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = (
            'pk',
            'name',
            'url',
            'created',
            'last_updated',
        )