from django.urls import path
from .views import user_login, task_list, user_logout, delete_task, update_task, signup_view, TaskListView  # Import TaskListView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('tasks/', task_list, name='task_list'),  # Updated to use the task_list function correctly
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
    
    # API Token Management
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API for tasks
    path('api/tasks/', TaskListView.as_view(), name='api_task_list'),
]
