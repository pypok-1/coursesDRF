from typing import Any

from rest_framework import serializers

from .models import Student, Course, Instructor


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('last_name', 'email')


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('last_name', 'email')


class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
