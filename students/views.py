from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentModelForm
from django.contrib import messages



def student_list(request):
    from .models import Student
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)

        entered_id = request.POST.get("id")

        # Check if ID already exists
        if Student.objects.filter(id=entered_id).exists():
            messages.error(request, f"ID {entered_id} already exists. Cannot add this student.")
            return redirect("students:add_student")

        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect("students:student_list")
    else:
        form = StudentModelForm()

    return render(request, "students/add_edit.html", {"form": form, "title": "Add Student"})

def edit_student(request, id):
    obj = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect('students:student_list')
    else:
        form = StudentModelForm(instance=obj)
    return render(request, 'students/add_edit.html', {'form': form, 'title': 'Edit Student'})


def delete_student(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect('students:student_list')
    return render(request, 'students/confirm_delete.html', {'object': obj})
