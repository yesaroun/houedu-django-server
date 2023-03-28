from django.db.models import QuerySet
from rest_framework.exceptions import NotFound, NotAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.serializers import SerializerMetaclass
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Course
from .serializers import CourseListSerializer, CourseDetailSerializer
from users.serializers import UserCourseSerializer


class CourseList(ListAPIView):
    """
    View to retrieve a list of courses.
    """

    queryset: QuerySet[Course] = Course.objects.all()
    serializer_class: SerializerMetaclass = CourseListSerializer


class MainCourseList(APIView):
    """
    메인 페이지에 보내는 코스 정보 view
    """

    def get(self, request):
        course = Course.objects.order_by("-id")[:4]
        serializer = CourseListSerializer(
            course,
            many=True,
        )
        return Response(serializer.data)


class CourseDetail(APIView):
    """
    Course 상세 정보 view(APIView를 상속 받아서)
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

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

    def post(self, request, pk):
        """
        Course 등록을 위한 POST API

        :param request:
        :param pk:
        :return:
        """
        course = self.get_object(pk)
        user = request.user
        serializer = UserCourseSerializer(
            data=request.data
            # user,
            # course,
        )
        if serializer.is_valid():
            enroll = serializer.save(user=user, course=course)
            serializer = UserCourseSerializer(enroll)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# class CourseDetail(RetrieveAPIView):
#     # class CourseDetail(APIView):
#     """
#     View to retrieve the details of a course.
#     """
#
#     queryset: QuerySet[Course] = Course.objects.all()
#     serializer_class: SerializerMetaclass = CourseDetailSerializer

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
