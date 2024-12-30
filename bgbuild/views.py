from django.shortcuts import render
from django.views import generic
from .models import Bgbuild

# Create your views here.
class BuildList(generic.ListView):
    queryset = Bgbuild.objects.all()
    template_name = "bgbuild/templates/bgbuild/build_list.html"
