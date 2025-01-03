# Generated by Django 4.2.17 on 2024-12-30 11:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bgbuild', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('content', models.TextField()),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='bgbuild.bgbuild')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
