from django.shortcuts import render

from .serializers import *
from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def trailers(request):
    trailers = Trailer.objects.all()
    serializer = TrailerSerializer(trailers, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def tractors(request):
    tractors = Tractor.objects.all()
    serializer = TractorSerializer(tractors, many=True)
    return Response(serializer.data)
