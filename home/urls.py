from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),          # Case 1: Home (no path)
    #path('index/', views.index, name='index'),    # Case 2: /index/ path
    path('about/', views.about, name='about'),    # Case 3: /about/ path
    path('contact/',views.contact,name='contact'),

]