from rest_framework import serializers
from .models import Course, Lecture
from users.serializers import TeacherNameSerializer, TeacherDetailSerializer
from categories.serializers import CategorySerializer
from typing import Tuple


class CourseNameSerializer(serializers.ModelSerializer):
    """
    코스 이름을 검색하는 Serializer
    """

    class Meta:
        model: Course = Course
        fields: Tuple[str] = (
            "id",
            "crs_name",
        )


from reviews.serializers import CourseDetailReviewSerializer


class CourseListSerializer(serializers.ModelSerializer):
    """
    코스 리스트를 조회하는 Serializer
    """

    tcr: TeacherNameSerializer = TeacherNameSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    count_reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model: Course = Course
        exclude: Tuple[str] = ("crs_info",)

    def get_count_reviews(self, course):
        return course.count_reviews()

    def get_rating(self, course):
        return course.rating()


class LectureDetailSerializer(serializers.ModelSerializer):
    """
    강의 리스트를 조회하는 Serializer
    """

    class Meta:
        model = Lecture
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    코스 세부 정보를 조회하는 Serializer
    """

    tcr = TeacherDetailSerializer(read_only=True)
    reviews = CourseDetailReviewSerializer(many=True)
    lectures = LectureDetailSerializer(many=True)
    category = CategorySerializer(read_only=True)
    count_reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model: Course = Course
        fields: Tuple[str] = "__all__"

    def get_count_reviews(self, course):
        return course.count_reviews()

    def get_rating(self, course):
        return course.rating()
