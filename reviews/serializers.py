from rest_framework import serializers
from .models import Review
from users.serializers import UserNickNameSerializer
from courses.serializers import CourseNameSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserNickNameSerializer(read_only=True)
    crs = CourseNameSerializer()

    class Meta:
        model: Review = Review
        fields: tuple = "__all__"


class ReviewStarSerializer(serializers.ModelSerializer):
    class Meta:
        model: Review = Review
        fields: tuple = ("star",)
