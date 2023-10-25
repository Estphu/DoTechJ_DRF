from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from .paginations import MyPageNumberPagination, MyLimitOffsetPagination
from rest_framework.generics import ListAPIView


# Create your views here.
class StudentAPIList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyLimitOffsetPagination


