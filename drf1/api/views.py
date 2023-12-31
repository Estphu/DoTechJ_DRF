from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
def student_detail(request,pk):
    std_obj = Student.objects.get(id=pk)
    serializer = StudentSerializer(std_obj)
    json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type ='application/json')
    # ANOTHER WAY DEVS DO ###########################################
    return JsonResponse(serializer.data)


def student_list(request):
    std_obj = Student.objects.all()
    serializer = StudentSerializer(std_obj,many=True)
    json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    ################################################################3
    return JsonResponse(serializer.data,safe=False)