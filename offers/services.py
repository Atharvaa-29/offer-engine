from rest_framework import viewsets
from .models import Offer
from .serializers import OfferSerializer
from . import controllers
from rest_framework.decorators import action
from rest_framework.response import Response

class OfferViewSet(viewsets.ViewSet):
    def list(self, request):
        return controllers.offers_list(request)

    def create(self, request):
        return controllers.offers_create(request)

    def update(self, request, pk=None):
        return controllers.offers_update(request, pk)

    def destroy(self, request, pk=None):
        return controllers.offers_delete(request, pk)
