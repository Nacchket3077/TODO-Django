from django.urls import path
from . import views

urlpatterns = [
  path('addTask/', views.addTask, name='addTask'),
  path('maek_as_done/<int:pk>/', views.maek_as_done, name='maek_as_done'),
  path('maek_as_undone/<int:pk>/', views.maek_as_undone, name='maek_as_undone'),
  path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
  path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]