from django.urls import path
from .views import BuildList
from . import views

urlpatterns = [
    path('', BuildList.as_view(), name="builds"),
]