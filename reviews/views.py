from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Review
from .serializers import ReviewSerializer
from typing import List


class Reviews(APIView):

    """전체 리뷰 리스트 apiview"""

    def get(self, request: HttpRequest) -> HttpResponse:
        all_reviews: QuerySet[Review] = Review.objects.all()
        serializer: List[ReviewSerializer] = ReviewSerializer(all_reviews, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest) -> HttpResponse:
        serializer: ReviewSerializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review: Review = serializer.save()
            return Response(ReviewSerializer(review).data)
        else:
            return Response(serializer.errors)


class ReviewDetail(APIView):

    """상세 리뷰 apiview"""

    def get_object(self, pk) -> Review:
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise NotFound

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
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

    def delete(self, request: HttpRequest, pk: int) -> HttpResponse:
        review: Review = self.get_object(pk)
        review.delete()
        return Response(status=HTTP_204_NO_CONTENT)
