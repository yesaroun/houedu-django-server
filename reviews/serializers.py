from rest_framework import serializers
from .models import Review
from users.serializers import UserNickNameSerializer
from courses.inlineSerializers import CourseNameSerializer
from typing import Tuple


class UserReviewsSerializer(serializers.ModelSerializer):
    """
    사용자의 리뷰를 조회하는 serializer
    """

    crs = CourseNameSerializer(read_only=True)

    class Meta:
        model = Review
        exclude: Tuple[str] = ("user",)


class ReviewSerializer(serializers.ModelSerializer):
    """
    모든 리뷰를 조회하는 serializer
    """

    user: UserNickNameSerializer = UserNickNameSerializer(read_only=True)
    crs: CourseNameSerializer = CourseNameSerializer()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model: Review = Review
        fields: Tuple[str] = "__all__"

    def get_is_owner(self, review):
        request = self.context["request"]
        return review.user == request.user


class CourseDetailReviewSerializer(serializers.ModelSerializer):
    """
    코스 디테일페이지에 해당 코스의 리뷰를 조회하는 serializer
    """

    user: UserNickNameSerializer = UserNickNameSerializer(read_only=True)
    crs: CourseNameSerializer = CourseNameSerializer()

    class Meta:
        model: Review = Review
        fields: Tuple[str] = "__all__"


class ReviewStarSerializer(serializers.ModelSerializer):
    """
    리뷰의 별점을 조회하는 serializer
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
