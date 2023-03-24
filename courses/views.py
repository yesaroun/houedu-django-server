from django.db.models import QuerySet
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import SerializerMetaclass
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course
from reviews.models import Review
from .serializers import CourseListSerializer, CourseDetailSerializer
from reviews.serializers import ReviewSerializer


class CourseList(ListAPIView):
    """
    View to retrieve a list of courses.
    """

    queryset: QuerySet[Course] = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseListSerializer


class CourseDetailBAV(APIView):
    """
    Course 상세 정보 view(APIView를 상속 받아서)
    """

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        """
        Course 상세 정보를 볼 수 있도록 하는 GET API

        :param request:
        :param pk:
        :return:
        """
        course = self.get_object(pk)
        serializer = CourseDetailSerializer(
            course,
        )
        return Response(serializer.data)


class CourseDetail(RetrieveAPIView):
    # class CourseDetail(APIView):
    """
    View to retrieve the details of a course.
    """

    queryset: QuerySet[Course] = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseDetailSerializer

    # 리뷰 8개만 불러오는 코드 (수정 필요)
    # def get_object(self, pk):
    #     try:
    #         return Course.objects.get(pk=pk)
    #     except Course.DoesNotExist:
    #         raise NotFound
    #
    # def get(self, request, pk):
    #     course = self.get_object(pk)
    #     serializer = CourseDetailSerializer(
    #         course,
    #         data=request.data,
    #         partial=True,
    #     )
    #     if serializer.is_valid():
    #         updated_courses = serializer.save()
    #         return Response(CourseDetailSerializer(updated_courses).data)
    #     else:
    #         return Response(serializer.errors)

    # def get(self, request, pk, *args, **kwargs):
    #     instance = self.get_object(pk)
    #     serializer = self.get_serializer(instance)
    #     reviews = Review.objects.filter(crs=instance)[:8]
    #     serialized_reviews = ReviewSerializer(reviews, many=True).data
    #     serialized_data = serializer.data
    #     serialized_data["reviews"] = serialized_reviews
    #     return Response(serialized_data)
