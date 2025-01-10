from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Bgbuild
from .forms import CommentForm
from django.contrib import messages


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
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.build = build
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "bgbuild/build_detail.html",
        {
            "build": build,
            "reviews": reviews,
            "reviews_count": reviews_count,
            "comment_form": comment_form,
        },
    )