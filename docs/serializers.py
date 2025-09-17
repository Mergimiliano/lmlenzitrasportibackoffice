from rest_framework import serializers
from .models import *

class TractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tractor
        fields = ["plate"]

class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = ["plate"]