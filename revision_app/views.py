from django.shortcuts import render
from .forms import EmployeeForm

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    else:
        form = EmployeeForm()

    return render(request, "add_employee.html", {"form": form})

