from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register(r'provider', api.ProviderViewSet)
router.register(r'amount', api.CheapestAmountViewSet, basename='amount')

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)
