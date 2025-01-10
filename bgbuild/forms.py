from .models import Bgbuild, Review
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)

class BgBuildForm(forms.ModelForm):
    """
    A form for creating and updating lego build posts.

    """
    class Meta:
        model = Bgbuild
        fields = ['build_title', 'slug', 'build_role', 'base_class',
                  'multiclass_one', 'multiclass_two', 'difficulty',
                  'excerpt', 'content']
        labels = {
            'build_title': "Build Title",
            'slug': "Slug (Title lowercase, and spaces replaced with '-')",
            'build_role': "Build Role",
            'base_class': "Base Class",
            'multiclass_one': "Multiclass One",
            'multiclass_two': "Multiclass Two",
            'difficulty': "Difficulty",
            "excerpt": "Excerpt",
            "content": "Build description",
        }
