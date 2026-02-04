from typing import Any

from rest_framework import serializers

from .models import Student, Course, Instructor


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'last_name', 'email')


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('id', 'name', 'last_name', 'email')

    def validate_experience(self, value):
        if value < 0:
            raise serializers.ValidationError("Experience cannot be --neg")
        return value


class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)
    students = StudentSerializer(many=True, read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all(), source='instructor',
                                                       write_only=True)
    student_ids = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='students', write_only=True,
                                                     many=True)

    class Meta:
        model = Course
        fields = ('id', 'title',
                  'description',
                  'start_date',
                  'instructor',
                  'students',
                  'instructor_id',
                  'student_ids')

    def create(self, validated_data):
        student_ids = validated_data.pop('student_ids', None)
        course = Course.objects.create(**validated_data)
        if student_ids:
            course.students.set(student_ids)
        return course

    def update(self, instance, validated_data):
        student_ids = validated_data.pop('student_ids', None)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        if student_ids is not None:
            instance.students.set(student_ids)
        instance.save()
        return instance
