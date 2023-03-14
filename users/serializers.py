from rest_framework.serializers import ModelSerializer
from .models import User, Teacher


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "nickname",
        )


class TeacherNameSerializer(ModelSerializer):
    class Meta:
        model: Teacher = Teacher
        fields: tuple = ("tcr_name",)
