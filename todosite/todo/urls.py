from django.urls import path
from .views import HomePageView, TaskCreateView, TaskDetailView, TaskDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('new/', TaskCreateView.as_view(), name = 'new-task'),
    path('<int:pk>/',TaskDetailView.as_view(), name = 'task-detail'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name = 'task-delete')
]

