from django.db.models import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import SerializerMetaclass
from .models import Course
from .serializers import CourseListSerializer, CourseDetailSerializer


class CourseList(ListAPIView):
    queryset: QuerySet = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseListSerializer


class CourseDetail(RetrieveAPIView):
    queryset: QuerySet = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseDetailSerializer
