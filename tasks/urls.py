from django.urls import path
from .views import TaskListView, TaskDetailView, UserRegisterView, UserLoginView
from .sort import SortedTaskListView

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("tasks/sorted/<str:sort_by>",SortedTaskListView.as_view(),name="task-sort")
]
