# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.list, name='list'),

# ]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("create/", views.task_create, name="task-create"),
    path("delete/<int:pk>/", views.task_delete, name="task-delete"),
    path("toggle/<int:pk>/", views.task_toggle, name="task-toggle"),
    path("edit/<int:pk>/", views.task_edit, name="task-edit"),
]