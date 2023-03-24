from rest_framework import serializers
from .models import Review
from users.serializers import UserNickNameSerializer
from courses.inlineSerializers import CourseNameSerializer
from typing import Tuple


class UserReviewsSerializer(serializers.ModelSerializer):
    crs = CourseNameSerializer(read_only=True)
    """ "
    유저가 받아오는 시리얼라이저
    """

    class Meta:
        model = Review
        exclude = ("user",)
        # fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve the review of a course.
    """

    user: UserNickNameSerializer = UserNickNameSerializer(read_only=True)
    crs: CourseNameSerializer = CourseNameSerializer()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model: Review = Review
        fields: Tuple[str, ...] = "__all__"

    def get_is_owner(self, review):
        request = self.context["request"]
        return review.user == request.user


class CourseDetailReviewSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve the review of a course.
    """

    user: UserNickNameSerializer = UserNickNameSerializer(read_only=True)
    crs: CourseNameSerializer = CourseNameSerializer()

    class Meta:
        model: Review = Review
        fields: Tuple[str, ...] = "__all__"


class ReviewStarSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving only the star rating from reviews.
    """

    class Meta:
        model: Review = Review
        fields: Tuple[str, ...] = (
            "id",
            "star",
        )


class ReviewOnlySerializer(serializers.ModelSerializer):
    """
    Review 정보만 있는 serializer
    """

    class Meta:
        model = Review
        fields = "__all__"
