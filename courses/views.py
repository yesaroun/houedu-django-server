# from django.db.models import QuerySet
# from rest_framework.generics import ListAPIView, RetrieveAPIView
# from rest_framework.serializers import SerializerMetaclass
# from .models import Course
# from .serializers import CourseSerializer
#
#
# class CourseList(ListAPIView):
#     queryset: QuerySet = Course.objects.all()
#     serializer_class: SerializerMetaclass = CourseSerializer
#
#
# class CourseDetail(RetrieveAPIView):
#     queryset: QuerySet = Course.objects.all()
#     serializer_class: SerializerMetaclass = CourseSerializer
