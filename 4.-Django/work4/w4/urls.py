from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="thisw4"),
    path("<str:name>", views.greet, name="greet"),
    path("Second", views.sec, name="Second"),
    path("third", views.third, name="Second"),
]