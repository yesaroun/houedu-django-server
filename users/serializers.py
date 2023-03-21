from rest_framework.serializers import ModelSerializer
from .models import User, Teacher


class PrivateUserSerializer(ModelSerializer):
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


class UserNickNameSerializer(ModelSerializer):
    class Meta:
        model: User = User
        fields: tuple = ("nickname",)


class TeacherNameSerializer(ModelSerializer):
    class Meta:
        model: Teacher = Teacher
        fields: tuple = ("tcr_name",)


class TeacherDetailSerializer(ModelSerializer):
    class Meta:
        model: Teacher = Teacher
        fields: tuple = ("tcr_name", "tcr_info", "tcr_img", "tcr_career")
