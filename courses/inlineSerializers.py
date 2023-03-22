from rest_framework import serializers
from .models import Course
from typing import Tuple


class CourseNameSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve the name of a course.
    """

    class Meta:
        model: Course = Course
        fields: Tuple[str, ...] = (
            "id",
            "crs_name",
        )
