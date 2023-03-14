from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model: Review = Review
        fields: tuple = ("__all__",)


class ReviewStarSerializer(serializers.ModelSerializer):
    class Meta:
        model: Review = Review
        fields: tuple = ("star",)
