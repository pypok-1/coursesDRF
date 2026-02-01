from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT)
    students = models.ManyToManyField(Student, related_name='courses')

    class Course(models.Model):
        def __str__(self):
            return self.title

