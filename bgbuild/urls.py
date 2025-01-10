from django.urls import path
from .views import BuildList, build_detail
from . import views

urlpatterns = [
    path('', BuildList.as_view(), name="builds"),
    path('<slug:slug>/', views.build_detail, name='build_detail'),
]