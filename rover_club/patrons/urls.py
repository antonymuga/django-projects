from django.urls import path
from . import views

urlpatterns = [
        path('', views.main, name='main'),
        path('patrons/', views.patrons, name='patrons'),
        path('patrons/details/<int:id>', views.details, name='details'),
        path('testing/', views.testing, name='testing'),
]
