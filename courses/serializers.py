from rest_framework import serializers
from .models import Course
from users.serializers import TeacherNameSerializer


class CourseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model: Course = Course
        fields: tuple = ("crs_name",)


from reviews.serializers import ReviewStarSerializer


class CourseSerializer(serializers.ModelSerializer):
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
        fields = "__all__"
