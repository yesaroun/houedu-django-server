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
        all_reviews: QuerySet[Review] = Review.objects.all().order_by("-created_at")
        serializer: ReviewSerializer = ReviewSerializer(
            all_reviews,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)


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
