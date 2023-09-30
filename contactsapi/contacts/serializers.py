from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):

    class Meta():
        model = Contact
        fields = ['country_code','owner','phone_number','first_name','last_name','contact_picture','is_favourite']