from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from rest_framework.exceptions import NotFound, NotAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer
from typing import List


class Reviews(APIView):

    """전체 리뷰 리스트 apiview"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        전체 리뷰를 볼 수 있도록 하는 GET API

        :param request:
        :return:
        """
        all_reviews: QuerySet[Review] = Review.objects.all()
        serializer: ReviewSerializer = ReviewSerializer(
            all_reviews,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    # 수정하기
    # 1. my info에서 post 할 수 있도록 하기
    # 2. 현재의 ReviewSerializer로는 생성하기 어려울 듯 수정하기
    def post(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            # 로그인 되어야만 post
            serializer: ReviewSerializer = ReviewSerializer(
                data=request.data,
            )
            if serializer.is_valid():
                review: Review = serializer.save(user=request.user)  # user 정보 자동으로 저장
                return Response(ReviewSerializer(review).data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class ReviewDetail(APIView):

    """상세 리뷰 apiview"""

    def get_object(self, pk) -> Review:
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise NotFound

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        """
        상세 리뷰를 볼 수 있도록 하는 GET API

        :param request:
        :param pk:
        :return:
        """
        review: Review = self.get_object(pk)
        serializer: ReviewSerializer = ReviewSerializer(
            review,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_review: Review = serializer.save()
            return Response(ReviewSerializer(updated_review).data)
        else:
            return Response(serializer.errors)

    # myinfo/myreviews/<int:pk> 로 넘겼다
    # def delete(self, request: HttpRequest, pk: int) -> HttpResponse:
    #     if request.user.is_authenticated:
    #         review: Review = self.get_object(pk)
    #         review.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         raise NotAuthenticated
