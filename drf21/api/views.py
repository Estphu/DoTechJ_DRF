from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
# class StudentAPIList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer





class StudentAPIList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']

    def get_queryset(self):
        return Student.objects.filter(pass_by=self.request.user)