from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError
from .serializers import PrivateUserSerializer


class User(APIView):
    """
    회원가입 API
    """

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        회원가입을 위한 POST API

        :param request: HTTP 요청 객체
        :type request: django.http.HttpRequest
        :return: HTTP 응답 객체
        :rtype: Union[django.http.JsonResponse, django.http.HttpResponse]
        """
        password: str = request.data.get("password")
        # 비밀번호 validation
        if not password:
            raise ParseError(detail="비밀번호를 입력해주세요.")
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


class ChangePassword(APIView):
    """
    비밀번호 변경 API
    """

    permission_classes = [IsAuthenticated]

    def put(self, request: HttpRequest) -> HttpResponse:
        """
        비밀번호 변경을 위한 PUT API

        :param request: HTTP 요청 객체
        :type request: django.http.HttpRequest
        :return: HTTP 응답 객체
        :rtype: Union[django.http.JsonResponse, django.http.HttpResponse]
        """
        user: User = request.user
        old_password: str = request.data.get("old_password")
        new_password: str = request.data.get("new_password")
        if not new_password or not old_password:
            raise ParseError
        if user.check_password(old_password):  # 로그인한 유저와 old_password가 같다면 비밀번호 변경
            user.set_password(new_password)
            user.save()
        else:
            raise ParseError
        return Response(status=status.HTTP_200_OK)


class LogIn(APIView):
    """
    로그인 API
    """

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"ok": "Welcome"})
        else:
            return Response({"error": "wrong password"})


class LogOut(APIView):
    """
    LogOut API
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "Logout"})
