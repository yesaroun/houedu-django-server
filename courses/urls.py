from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CourseList, CourseDetail, CourseDetailBAV


urlpatterns: list[URLPattern] = [
    path("", CourseList.as_view()),
    # path("<int:pk>/", CourseDetail.as_view()),
    path("<int:pk>/", CourseDetailBAV.as_view()),
]
