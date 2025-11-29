from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentModelForm
from django.contrib import messages
from django.urls import reverse

def student_list(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'students/list.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('students:student_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentModelForm()
    return render(request, 'students/add_edit.html', {'form': form, 'title': 'Add Student'})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect('students:student_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/add_edit.html', {'form': form, 'title': 'Edit Student'})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect('students:student_list')
    return render(request, 'students/confirm_delete.html', {'object': student})
