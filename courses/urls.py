from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CourseList, CourseDetail, MainCourseList


urlpatterns: list[URLPattern] = [
    path("", CourseList.as_view()),
    path("mainlist/", MainCourseList.as_view()),
    path("<int:pk>/", CourseDetail.as_view()),
]
