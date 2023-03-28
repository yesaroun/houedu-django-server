from rest_framework import serializers
from .models import Category
from typing import Tuple


class CategorySerializer(serializers.ModelSerializer):
    """
    Category 모델에 대한 Serializer
    """

    class Meta:
        model = Category
        fields: Tuple[str] = ("id", "name")
