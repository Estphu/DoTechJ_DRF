from rest_framework import serializers
from .models import Student

# validators
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Must starts with R')
    return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128,validators=[starts_with_r])
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=128)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll_no = validated_data.get('roll_no',instance.roll_no)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
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