from django.http import HttpResponse, HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError
from .serializers import PrivateUserSerializer


class User(APIView):

    """
    회원가입, 로그인 API
    """

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        회원가입을 위한 POST API

        :param request: HTTP 요청 객체
        :type request: django.http.HttpRequest
        :return: HTTP 응답 객체
        :rtype: Union[django.http.JsonResponse, django.http.HttpResponse]
        """
        password = request.data.get("password")
        # 비밀번호 validation
        if not password:
            raise ParseError
        else:
            serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MyInfo(APIView):
    """
    사용자 정보 조회, 수정 API
    """

    permission_classes = [IsAuthenticated]
    # 로그인 여부 확인

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        사용자가 자신의 정보를 볼 수 있도록 하는 GET API

        :param request: HTTP 요청 객체
        :type request: django.http.HttpRequest
        :return: HTTP 응답 객체
        :rtype: Union[django.http.JsonResponse, django.http.HttpResponse]
        """
        user: User = request.user
        serializer: PrivateUserSerializer = PrivateUserSerializer(user).data
        return Response(serializer)

    def put(self, request: HttpRequest) -> HttpResponse:
        """
        사용자가 자신의 정보를 수정할 수 있도록 하는 PUT API

        :param request: HTTP 요청 객체
        :type request: django.http.HttpRequest
        :return: HTTP 응답 객체
        :rtype: Union[django.http.JsonResponse, django.http.HttpResponse]
        """
        user: User = request.user
        serializer: PrivateUserSerializer = PrivateUserSerializer(
            user, data=request.data, partial=True
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
