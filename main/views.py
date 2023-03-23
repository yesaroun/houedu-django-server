from rest_framework.views import APIView
from django.shortcuts import render


# class Main(APIView):
#     pass


def home(request):
    return render(request, "index.html")
