from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('health/', views.health_check, name='health-check'),
]