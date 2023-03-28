from rest_framework import serializers
from .models import User, Teacher, UserCourse
from courses.inlineSerializers import CourseNameSerializer
from typing import Tuple


class UserCourseSerializer(serializers.ModelSerializer):
    """
    사용자가 등록한 코스 serializer
    """

    course = CourseNameSerializer(read_only=True)

    class Meta:
        model = UserCourse
        fields: Tuple[str] = (
            "id",
            "course",
        )


class PrivateUserSerializer(serializers.ModelSerializer):
    """
    사용자 정보 serializer
    """

    userCourses = UserCourseSerializer(read_only=True, many=True)

    class Meta:
        model = User
        exclude: Tuple[str] = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )


class UserNickNameSerializer(serializers.ModelSerializer):
    """
    사용자의 nickname serializer
    """

    class Meta:
        model: User = User
        fields: Tuple[str] = (
            "id",
            "nickname",
        )


class UserCoursesSerializer(serializers.ModelSerializer):
    """
    사용자가 등록한 코스들 serializer
    """

    crs = CourseNameSerializer(read_only=True)

    class Meta:
        model = UserCourse
        fields = "__all__"


from reviews.serializers import UserReviewsSerializer


class MyReviewSerializer(serializers.ModelSerializer):
    user = PrivateUserSerializer(read_only=True)
    reviews = UserReviewsSerializer(many=True)
    userCourses = UserCourseSerializer(read_only=True, many=True)

    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
            "last_login",
            "date_joined",
        )


class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model: Teacher = Teacher
        fields: tuple = (
            "id",
            "tcr_name",
        )


class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model: Teacher = Teacher
        fields: tuple = ("tcr_name", "tcr_info", "tcr_img", "tcr_career")
