from rest_framework import serializers
from .models import Course
from typing import Tuple


class CourseNameSerializer(serializers.ModelSerializer):
    """
    코스 이름을 위한 serializer
    """

    class Meta:
        model: Course = Course
        fields: Tuple[str, ...] = (
            "id",
            "crs_name",
        )
