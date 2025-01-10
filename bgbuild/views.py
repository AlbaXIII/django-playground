from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Bgbuild

# Create your views here.
class BuildList(generic.ListView):
    queryset = Bgbuild.objects.all().order_by("-created_on")
    template_name = "bgbuild/build_list.html"

def build_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Bgbuild.objects.filter(status=1)
    build = get_object_or_404(queryset, slug=slug)
    reviews = build.reviews.all().order_by("review_date")
    reviews_count = build.reviews.filter(approved=True).count()

    return render(
        request,
        "bgbuild/build_detail.html",
        {
            "build": build,
            "reviews": reviews,
            "reviews_count": reviews_count,
        },
    )