from django.urls import path
from . import views
app_name = 'Day9'
urlpatterns = [
    # Authentication
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('', views.dashboard, name='dashboard'),

    # Static pages
    path('', views.home_view, name='home'),  # Home page
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    # Task CRUD
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/edit/<int:pk>/', views.edit_task, name='edit_task'),

    # Session examples
    path('session/set/', views.set_session_example, name='session_set'),
    path('session/get/', views.get_session_example, name='session_get'),
    path('session/clear/', views.clear_session, name='session_clear'),

    
]
