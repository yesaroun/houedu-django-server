from django.conf import settings
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError, NotAuthenticated, NotFound
from .serializers import PrivateUserSerializer, MyReviewSerializer
from reviews.serializers import ReviewOnlySerializer, ReviewSerializer
from reviews.models import Review
from .models import User
from typing import Union
import jwt
import requests


class Users(APIView):
    """
    회원가입 API
    """

    def post(self, request: HttpRequest) -> Union[JsonResponse, HttpResponse]:
        """
        회원가입을 위한 POST API

        :param request: HTTP 요청 객체
        :type request: django.http.HttpRequest
        :return: HTTP 응답 객체
        :rtype: Union[django.http.JsonResponse, django.http.HttpResponse]
        :raise ParseError: 비밀번호가 입력되지 않은 경우
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
    회원 정보 조회, 수정 API
    """

    permission_classes = [IsAuthenticated]
    # 로그인 여부 확인

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        회원이 자신의 정보를 볼 수 있도록 하는 GET API

        :param request: HTTP 요청 객체
        :type request: django.http.HttpRequest
        :return: HTTP 응답 객체
        :rtype: Union[django.http.JsonResponse, django.http.HttpResponse]
        """
        user = request.user
        serializer: PrivateUserSerializer = PrivateUserSerializer(user).data
        return Response(serializer)

    def put(self, request: HttpRequest) -> HttpResponse:
        """
        회원이 자신의 정보를 수정할 수 있도록 하는 PUT API

        :param request: HTTP 요청 객체
        :type request: django.http.HttpRequest
        :return: HTTP 응답 객체
        :rtype: Union[django.http.JsonResponse, django.http.HttpResponse]
        """
        user = request.user
        serializer: PrivateUserSerializer = PrivateUserSerializer(
            user, data=request.data, partial=True
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer: PrivateUserSerializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# class MyCourses(APIView):
#     """
#     내 수강 강의 API
#     """
#
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         user = request.user
#         serializer = UserCoursesSerializer(user).data
#         return Response(serializer)


class MyReviews(APIView):
    """
    회원 자신의 리뷰 API
    """

    permission_classes = [IsAuthenticated]

    def get(self, request) -> HttpResponse:
        """
        회원의 리뷰 목록을 볼 수 있도록 하는 GET API

        :param request: HTTP 요청 객체
        :type request: django.http:HttpRequest
        :return: HTTP 응답 객체
        :rtype: Union[django.http.JsonResponse, django.http.HttpResponse]
        """
        user = request.user
        my_reviews = Review.objects.filter(user=user)
        # serializer: MyReviewSerializer = MyReviewSerializer(user).data
        serializer: ReviewSerializer = ReviewSerializer(
            my_reviews, many=True, context={"request": request}
        ).data
        return Response(serializer)

    def post(self, request):
        """
        회원이 리뷰를 작성할 수 있도록 하는 POST API

        :param request:
        :return:
        """
        user = request.user
        data = request.data.copy()
        data["user"] = user.id
        serializer = ReviewOnlySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyReviewsDetail(APIView):
    """
    회원 자신의 리뷰 detail API
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise NotFound

    def delete(self, request: HttpRequest, pk: int) -> HttpResponse:
        """
        회원이 자신의 리뷰를 삭제할 수 있도록 하는 DELETE API

        :param request:
        :param pk:
        :return:
        """
        if request.user.is_authenticated:
            review: Review = self.get_object(pk=pk)
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise NotAuthenticated


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
        :raise ParseError: 비밀번호가 일치하지 않은 경우
        """
        user = request.user
        old_password: str = request.data.get("old_password")
        new_password: str = request.data.get("new_password")
        if not new_password or not old_password:
            raise ParseError(detail="비밀번호가 일치하지 않습니다.")
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
        """
        사용자 로그인을 위한 POST API

        :param request: HTTP 요청 객체
        :return:
        """
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
            return Response(
                {"error": "wrong password"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogOut(APIView):
    """
    로그아웃 API
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        로그아웃을 위한 POST API
        :param request:
        :return:
        """
        logout(request)
        return Response({"ok": "Logout"})


class JWTLogin(APIView):
    """
    use JWT Login API
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
            token = jwt.encode(
                {"pk": user.pk},
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            return Response({"token": token})
        else:
            return Response({"error": "wrong password"})


class GithubLogIn(APIView):
    def post(self, request):
        """
        Github 로그인을 위한 POST API

        :param request:
        :return:
        """
        try:
            print("hi")
            code = request.data.get("code")
            access_token = requests.post(
                f"https://github.com/login/oauth/access_token?code={code}&client_id=b40759dbc613bb53f81d&client_secret={settings.GH_SECRET}",
                headers={"Accept": "application/json"},
            )
            access_token = access_token.json().get("access_token")
            user_data = requests.get(
                "https://api.github.com/user",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_data = user_data.json()
            user_emails = requests.get(
                "https://api.github.com/user/emails",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_emails = user_emails.json()
            try:
                print("start try")
                user = User.objects.get(email=user_emails[0]["email"])
                login(request, user)
                print("end login")
                return Response(status=status.HTTP_200_OK)
            except User.DoesNotExist:
                user = User.objects.create(
                    username=user_data.get("login"),
                    email=user_emails[0]["email"],
                    nickname=user_data.get("name"),
                    # img=user_data.get("avatar_url"),
                )
                print("make user 4")
                user.set_unusable_password()
                user.save()
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class KakaoLogIn(APIView):
    def post(self, request):
        """
        Kakao 로그인을 위한 POST API

        :param request:
        :return:
        """

        try:
            code = request.data.get("code")
            access_token = requests.post(
                "https://kauth.kakao.com/oauth/token",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={
                    "grant_type": "authorization_code",
                    "client_id": "ec72411cc6b187772440b8c3801b3090",
                    "redirect_uri": "http://127.0.0.1:3000/social/kakao",
                    "code": code,
                },
            )
            access_token = access_token.json().get("access_token")
            user_data = requests.get(
                "https://kapi.kakao.com/v2/user/me",
                headers={
                    "Authorization": f"Bearer ${access_token}",
                    "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
                },
            )
            user_data = user_data.json()
            kakao_account = user_data.get("kakao_account")
            profile = kakao_account.get("profile")
            print("user_data", user_data)
            try:
                print("유저가 있는 경우1")
                user = User.objects.get(email=kakao_account.get("email"))
                login(request, user)
                print("로그인 성공")
                return Response(status=status.HTTP_200_OK)
            # except Exception("땡땡"):
            #     print("hi")
            except User.DoesNotExist:
                print("회원가입 시작")
                user = User.objects.create(
                    email=kakao_account.get("email"),
                    username=kakao_account.get("email"),
                    nickname=profile.get("nickname"),
                    # avatar=profile.get("profile_image_url")
                )
                print("user", user)
                user.set_unusable_password()
                user.save()
                print("로그인 직전")
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        except Exception:
            print("love DH")
            return Response(status=status.HTTP_400_BAD_REQUEST)
