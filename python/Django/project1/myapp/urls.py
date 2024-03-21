from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.square),
    path('squarenum/', views.squareNum)
  
]