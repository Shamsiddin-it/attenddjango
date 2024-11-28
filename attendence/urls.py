from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
# URL Configuration
urlpatterns = [
    path('', HomeView.as_view() , name = 'home'),
    # Teacher URLs
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),

    # Course URLs
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),

    # Student URLs
    path('students/', StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    # Attendance URLs
    path('attendances/', AttendanceListView.as_view(), name='attendance_list'),
    path('attendance/create/', AttendanceCreateView.as_view(), name='attendance_create'),
    # Attendance detail view
    path('attendance/<int:pk>/', attendence_detail, name='attendance_detail'),
    path('attendance/<int:pk>/update/', AttendenceUpdateView.as_view(), name='attendance_update'),
    path('attendance/<int:pk>/delete/', AttendenceDeleteView.as_view(), name='attendance_delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', register, name = 'signup'),

]
