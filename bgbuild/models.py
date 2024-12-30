from django.db import models
from django.contrib.auth.models import User

# Dropdown fields
BUILD_ROLES = [
    ('melee', 'Melee'),
    ('ranged', 'Ranged'),
    ('support', 'Support'),
]

BASE_CLASS = [
    ('barbarian', 'Barbarian'),
    ('bard', 'Bard'),
    ('cleric', 'Cleric'),
    ('druid', 'Druid'),
    ('fighter', 'Fighter'),
    ('monk', 'Monk'),
    ('n/a', 'N/A'),
    ('paladin', 'Paladin'),
    ('ranger', 'Ranger'),
    ('rogue', 'Rogue'),
    ('sorcerer', 'Sorcerer'),
    ('warlock', 'Warlock'),
    ('wizard', 'Wizard')
]

DIFFICULTY = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
    ('expert', 'Expert')
]

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Bgbuild(models.Model):
    """
    A model to create and manage Baldur's Gate 3 build posts.
    """
    user = models.ForeignKey(
        User, related_name='build_owner', on_delete=models.CASCADE)
    build_title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(max_length=250, unique=True)
    build_role = models.CharField(
        max_length=50, choices=BUILD_ROLES, default="Melee")
    base_class = models.CharField(
        max_length=10, choices=BASE_CLASS, default="Barbarian")
    multiclass_one = models.CharField(
        max_length=10, choices=BASE_CLASS, default="N/A")
    multiclass_two = models.CharField(
        max_length=10, choices=BASE_CLASS, default="N/A")
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY, default="easy")
    excerpt = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)