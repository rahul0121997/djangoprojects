from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.student_create,name='student_create')
]
