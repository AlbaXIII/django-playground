from django.urls import path
from .views import BuildList, build_detail, AddBuild
from . import views

urlpatterns = [
    path('', BuildList.as_view(), name="builds"),
    path('add/', AddBuild.as_view(), name="add_build"),
    path('<slug:slug>/', views.build_detail, name='build_detail'),
]