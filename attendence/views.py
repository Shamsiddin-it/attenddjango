from django.urls import path
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Teacher, Course, Student, Attendence, User
from django.http import HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Teacher Views
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher_detail.html'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['name', 'age', 'phone', 'address', 'is_active']
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['name', 'age', 'phone', 'address', 'is_active']
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')
    
class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')

# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'

class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'time', 'price', 'description', 'max_students', 'min_students', 'teacher', 'start', 'end', 'is_active']
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')
    
class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name', 'time', 'price', 'description', 'max_students', 'min_students', 'teacher', 'start', 'end', 'is_active']
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('course_list')

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'age', 'phone', 'address', 'course', 'is_active']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'age', 'phone', 'address', 'course', 'is_active']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

# Attendance Views
class AttendanceListView(ListView):
    model = Attendence
    template_name = 'attendance_list.html'
    
    

class AttendanceCreateView(CreateView):
    model = Attendence
    fields = ['student', 'status', 'reason']
    template_name = 'attendance_form.html'
    success_url = reverse_lazy('attendance_list')
    def form_valid(self, form):
        # Set time to current time when a new attendance record is created
        form.instance.time = datetime.now()
        return super().form_valid(form)

class AttendenceUpdateView(UpdateView):
    model = Attendence
    fields = ['student', 'status', 'reason']
    template_name = 'attendance_form.html'
    success_url = reverse_lazy('attendance_list')

# Attendance Detail View
def attendence_detail(request, pk):
    attendance = get_object_or_404(Attendence, pk=pk)
    return render(request, 'attendance_detail.html', {'object': attendance})

# Attendance Delete View
class AttendenceDeleteView(DeleteView):
    model = Attendence
    template_name = 'attendance_confirm_delete.html'
    success_url = reverse_lazy('attendance_list')  # Redirect after deletion




class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the logged-in user (student)
        context['username'] = self.request.user.username
        user = self.request.user
        # Fetch the attendance records for this user
        attendance_records = Attendence.objects.filter()
        # Pass the attendance records to the context
        context['attendance_records'] = attendance_records
        return context


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class HomeView(TemplateView):
    template_name = "home.html"


