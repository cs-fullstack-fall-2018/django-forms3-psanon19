from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]