import logging
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from .models import Student, Instructor, Course
from .serializers import StudentSerializer, CourseSerializer, InstructorSerializer


class CourseListAPIView(APIView):

    def get(self, request):
        course = Course.objects.all()
        courses_serializer = CourseSerializer(course, many=True)
        return Response(courses_serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CourseDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Course, pk=pk)

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course,  partial=True, data=request.data )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

