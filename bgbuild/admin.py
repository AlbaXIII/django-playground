from django.contrib import admin
from .models import Bgbuild, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Bgbuild)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('build_title', 'slug', 'status', 'created_on')
    search_fields = ['build_title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug':('build_title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Review)