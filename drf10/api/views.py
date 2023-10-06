from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView
                                    #  , RetrieveUpdateAPIView,
                                    #  RetrieveDestroyAPIView
                                     )

class StudentAPIList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


####### MORE GENERIC CUSTOMIZE VIEWS EXAMPLE ###### 

# class StudentAPIRetreiveUpdate(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentAPIRetreiveDestroy(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer    
       

