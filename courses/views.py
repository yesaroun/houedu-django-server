from django.db.models import QuerySet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.serializers import SerializerMetaclass
from .models import Course
from .serializers import CourseSerializer


class CourseList(ListCreateAPIView):
    queryset: QuerySet = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseSerializer

    def get_queryset(self) -> QuerySet:
        return self.queryset

    def get_serializer_class(self) -> SerializerMetaclass:
        return self.serializer_class


class CourseDetail(RetrieveUpdateDestroyAPIView):
    queryset: QuerySet = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseSerializer

    def get_object(self) -> Course:
        return super().get_object()

    def get_serializer(self) -> CourseSerializer:
        return super().get_serializer()
