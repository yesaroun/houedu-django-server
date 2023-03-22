from rest_framework import serializers
from .models import User, Teacher, UserCourse
from courses.inlineSerializers import CourseNameSerializer


class UserCourseSerializer(serializers.ModelSerializer):
    course = CourseNameSerializer(read_only=True)

    class Meta:
        model = UserCourse
        fields = ("id", "course")


class PrivateUserSerializer(serializers.ModelSerializer):
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
        )


class UserNickNameSerializer(serializers.ModelSerializer):
    class Meta:
        model: User = User
        fields: tuple = (
            "id",
            "nickname",
        )


from reviews.serializers import UserReviewsSerializer


class MyReviewSerializer(serializers.ModelSerializer):
    user = PrivateUserSerializer(read_only=True)
    reviews = UserReviewsSerializer(many=True)

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


# class UserCoursesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "username", "nickname", "userCourses")
