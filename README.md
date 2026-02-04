# Online Courses API — Django REST Framework (Homework)



## Models

Suggested model fields (you can adapt types as needed):

- Instructor
  - name: CharField
  - email: EmailField (unique recommended)
  - experience_years: IntegerField (>= 0)

- Student
  - name: CharField
  - email: EmailField (unique recommended)
  - registration_date: DateField / DateTimeField (auto_now_add recommended)

- Course
  - title: CharField
  - description: TextField
  - start_date: DateField / DateTimeField
  - instructor: ForeignKey -> Instructor
  - students: ManyToManyField -> Student

---
