from django.urls import path
from . import views

urlpatterns = [
    path('addtask/', views.addtask, name='addtask'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('undo/<int:pk>/', views.undo, name='undo'),
    path('delete/<int:pk>/', views.delete, name="delete")
]