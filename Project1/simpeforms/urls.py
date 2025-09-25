from django.urls import path
from . import views

urlpatterns = [
    path('',views.form,name='forms'),
    path('models/', views.models, name='models'),
]


