from rest_framework import serializers
from .models import Review
from users.serializers import UserNickNameSerializer
from courses.serializers import CourseNameSerializer
from typing import Tuple


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
