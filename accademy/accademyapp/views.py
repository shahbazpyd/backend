# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def hello(request):
#     print("hello")
#     return HttpResponse("hello this is accademy project")


from functools import partial

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer



@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hello DRF"})

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many= True)
    #     return Response({"message": "Course list", "data": serializer.data})

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response({"message": "Single course", "data": serializer.data})
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data = request.data)
    #     serializer.is_valid(raise_exception = True)
    #     self.perform_create(serializer)
    #     return Response(
    #         {"message": "Course created", "data": serializer.data},
    #         status = status.HTTP_201_CREATED
    #     )

    # def update(self, request, *args, **kwargs):
    #     partial = False
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data = request.data, partial = partial)
    #     serializer.is_valid(raise_exception = True)
    #     self.perform_update(serializer)
    #     return Response({"message": "Course updated", "data": serializer.data})
    
    # def partial_update(self, request, *args, **kwargs):
    #     partial = True
    #     instance = self.get_query()
    #     serializer = self.get_serializer(instance, data = request.data, partial = partial)
    #     serializer.is_valid(raise_exception = True)
    #     self.perform_update(serializer)
    #     return Response({"message": "Course partially updated", "data": serializer.data})
    
    def destroy(self, request, *args, **kwargs):
        instanse = self.get_object()
        self.perform_destroy(instanse)
        return Response({"message": "Course deleted"})


        

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


