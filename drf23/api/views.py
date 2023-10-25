from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from .paginations import MyPageNumberPagination
from rest_framework.generics import ListAPIView


# Create your views here.
class StudentAPIList(ListAPIView, MyPageNumberPagination):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination


