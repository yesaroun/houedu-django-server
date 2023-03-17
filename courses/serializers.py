from rest_framework import serializers
from .models import Course
from users.serializers import TeacherNameSerializer, TeacherDetailSerializer
from typing import Tuple


class CourseNameSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve the name of a course.
    """

    class Meta:
        model: Course = Course
        fields: Tuple[str, ...] = ("crs_name",)


from reviews.serializers import ReviewStarSerializer, ReviewSerializer


class CourseListSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve a list of courses.
    """

    tcr: TeacherNameSerializer = TeacherNameSerializer(read_only=True)
    reviews: ReviewStarSerializer = ReviewStarSerializer(read_only=True, many=True)

    class Meta:
        model: Course = Course
        exclude: Tuple[str, ...] = ("crs_info",)


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve a list of courses.
    """

    tcr: TeacherDetailSerializer = TeacherDetailSerializer(read_only=True)
    reviews: ReviewSerializer = ReviewSerializer(many=True)

    class Meta:
        model: Course = Course
        fields: Tuple[str, ...] = "__all__"
