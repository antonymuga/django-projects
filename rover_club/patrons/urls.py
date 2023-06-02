from django.urls import path
from . import views

urlpatterns = [
        path("patrons/", views.patrons, name="patrons"),
        path('patrons/details/<int:id>', views.details, name='details'),
]
