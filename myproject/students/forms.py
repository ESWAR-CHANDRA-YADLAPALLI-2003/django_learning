from django import forms
from .models import Student
from django.core.exceptions import ValidationError

def validate_name_no_digits(value):
    if any(ch.isdigit() for ch in value):
        raise ValidationError("Name cannot contain numbers.")

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'marks', 'email', 'city']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 5, 'max': 100}),
            'marks': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if any(c.isdigit() for c in name):
            raise forms.ValidationError("Name should not contain numbers.")
        return name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and (age < 5 or age > 100):
            raise forms.ValidationError("Age must be between 5 and 100.")
        return age

    def clean_marks(self):
        marks = self.cleaned_data.get('marks')
        if marks is not None and (marks < 0 or marks > 100):
            raise forms.ValidationError("Marks must be between 0 and 100.")
        return marks
