from django.db.models import QuerySet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.serializers import SerializerMetaclass
from .models import Course
from .serializers import CourseSerializer


class CourseList(ListCreateAPIView):
    queryset: QuerySet = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseSerializer


class CourseDetail(RetrieveUpdateDestroyAPIView):
    queryset: QuerySet = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseSerializer
