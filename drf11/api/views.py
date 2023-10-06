from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

def detailaboutfunction(self):
        print(f'*******{self.action} VIEW **********')
        print(f'BASE NAME: {self.basename}')
        print(f'Detail: {self.detail}')
        print(f'Suffix: {self.suffix}')
        print(f'Name: {self.name}')
        print(f'Description: {self.description}')

class StudentViewset(viewsets.ViewSet):

    def list(self, request):
        detailaboutfunction(self)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        detailaboutfunction(self)
        if pk is not None:    
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request, pk):
        detailaboutfunction(self)
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'},serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        detailaboutfunction(self)
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'},serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        detailaboutfunction(self)
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'},serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        detailaboutfunction(self)
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg': 'Data Deleted'})               

