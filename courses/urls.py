# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListAPIView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailAPIView.as_view(), name='course_detail'),
]