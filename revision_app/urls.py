from django.urls import path
from .views import add_employee

urlpatterns = [
    path('add-employee/', add_employee, name='add_employee'),
    
]
