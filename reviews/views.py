from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from typing import List


class Reviews(APIView):
    def get(self: Review, request: HttpRequest) -> HttpResponse:
        all_reviews: QuerySet[Review] = Review.objects.all()
        serializer: List[ReviewSerializer] = ReviewSerializer(all_reviews, many=True)
        return Response(serializer.data)

    def post(self: Review, request: HttpRequest) -> HttpResponse:
        serializer: List[ReviewSerializer] = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save()
            return Response(ReviewSerializer(review).data)
        else:
            return Response(serializer.errors)
