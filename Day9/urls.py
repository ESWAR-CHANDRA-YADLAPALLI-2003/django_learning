from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('session/set/', views.set_session_example, name='session_set'),
    path('session/get/', views.get_session_example, name='session_get'),
    path('session/clear/', views.clear_session, name='session_clear'),
    path('register/', views.register_user, name='register'),
    path('', views.home_view, name='home'),  # home page
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

]
