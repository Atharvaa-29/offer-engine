from rest_framework.response import Response
from rest_framework import status
from .models import Offer
from .serializers import OfferSerializer
from django.shortcuts import get_object_or_404

def offers_list(request):
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return Response(serializer.data)

def offers_create(request):
    serializer = OfferSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def offers_update(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    serializer = OfferSerializer(offer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def offers_delete(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    offer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)