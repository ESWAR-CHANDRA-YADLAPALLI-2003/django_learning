from django import forms
from .models import Student
from django.core.exceptions import ValidationError

def validate_name_no_digits(value):
    if any(ch.isdigit() for ch in value):
        raise ValidationError("Name must not contain numbers.")

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'marks', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if any(c.isdigit() for c in name):
            raise forms.ValidationError("Name cannot contain digits.")
        return name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and (age < 5 or age > 100):
            raise forms.ValidationError("Age must be between 5 and 100.")
        return age
