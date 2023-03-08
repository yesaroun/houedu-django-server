from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model: Course = Course
        fields: list = ["id", "tcr", "crs_name", "crs_info", "thumbnail"]
