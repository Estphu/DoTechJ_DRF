from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll_no = serializers.PositiveIntegerField()
    city = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)