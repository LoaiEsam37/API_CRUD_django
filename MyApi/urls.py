from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.apiOverview, name="apiOverview"),
    
    # CRUD (Task Model) >>>

    # Create (Task Model)
    path('task-create/', views.TaskCreate, name="TaskCreate"),
    # Read (Task Model)
    path('task-detail/<str:id>/', views.TaskDetail, name="TaskDetail"),
    path('task-overview/', views.TaskOverview, name="TaskOverview"),
    # Update (Task Model)
    path('task-update/<str:id>/', views.TaskUpdate, name="TaskUpdate"),
    # Delete (Task ModeL)
    path('task-delete/<str:id>/', views.TaskDelete, name="TaskDelete"),

    # CRUD (Task Model) <<<

]