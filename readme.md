
users/serializers.py
```python
from rest_framework import serializers
from .models import User, Teacher, UserCourse
from courses.serializers import CourseNameSerializer


class UserCourseSerializer(serializers.ModelSerializer):
    courses = CourseNameSerializer(read_only=True)

    class Meta:
        model = UserCourse
        fields = "__all__"


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
```

courses/serializers.py
```python
from rest_framework import serializers
from .models import Course, Lecture
from users.serializers import TeacherNameSerializer, TeacherDetailSerializer
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


from reviews.serializers import ReviewStarSerializer, ReviewSerializer


class CourseListSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve a list of courses.
    """

    tcr: TeacherNameSerializer = TeacherNameSerializer(read_only=True)
    # reviews: ReviewStarSerializer = ReviewStarSerializer(read_only=True, many=True)
    count_reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model: Course = Course
        exclude: Tuple[str, ...] = ("crs_info",)

    def get_count_reviews(self, course):
        return course.count_reviews()

    def get_rating(self, course):
        return course.rating()


class LectureDetailSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve a list of lectures.
    """

    class Meta:
        model = Lecture
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve a list of courses.
    """

    tcr: TeacherDetailSerializer = TeacherDetailSerializer(read_only=True)
    reviews: ReviewSerializer = ReviewSerializer(many=True)
    lectures = LectureDetailSerializer(many=True)
    count_reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model: Course = Course
        fields: Tuple[str, ...] = "__all__"

    def get_count_reviews(self, course):
        return course.count_reviews()

    def get_rating(self, course):
        return course.rating()

```

이 django 프로젝트의 경우 ImportError: cannot import name 'CourseNameSerializer' from partially initialized module 'courses.serializers' (most likely due to a circular import) (/Users/akor1/Documents/programing/code/prj/houedu-django-server/courses/serializers.py)
이 에러는 왜 생기는걸까?
