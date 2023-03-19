from django.db.models import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import SerializerMetaclass
from .models import Course
from .serializers import CourseListSerializer, CourseDetailSerializer


class CourseList(ListAPIView):
    """
    View to retrieve a list of courses.
    """

    queryset: QuerySet[Course] = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseListSerializer


class CourseDetail(RetrieveAPIView):
    """
    View to retrieve the details of a course.
    """

    queryset: QuerySet[Course] = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseDetailSerializer
