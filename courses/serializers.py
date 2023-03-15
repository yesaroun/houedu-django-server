from rest_framework import serializers
from .models import Course
from users.serializers import TeacherNameSerializer, TeacherDetailSerializer


class CourseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model: Course = Course
        fields: tuple = ("crs_name",)


from reviews.serializers import ReviewStarSerializer, ReviewSerializer


class CourseListSerializer(serializers.ModelSerializer):
    tcr = TeacherNameSerializer(read_only=True)
    reviews = ReviewStarSerializer(read_only=True, many=True)

    class Meta:
        model: Course = Course
        # fields: tuple = (
        #     "id",
        #     "crs_name",
        #     "crs_info",
        #     "thumbnail",
        #     "tcr",
        # )
        exclude = ("crs_info",)
        # fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    tcr = TeacherDetailSerializer(read_only=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model: Course = Course
        fields = "__all__"
