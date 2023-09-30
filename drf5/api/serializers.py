from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # validators
    def starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Must starts with R')
        return value



    name = serializers.CharField(read_only=True,validators=[starts_with_r])

    class Meta():
        model = Student
        fields = ['name','roll_no','city']
    
    # Field Level Validation
    def validate_roll_no(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seats Full')
        return value
        
    # Object Level Validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == "kyle" and city.lower() != "toronto":
            raise serializers.ValidationError('City must be Toronto!')
        return data