# Generated by Django 3.2.8 on 2021-12-15 12:17

import cloudinary_storage.storage
import cloudinary_storage.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import video.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('now', models.IntegerField(default=0, verbose_name='Current progress')),
                ('total', models.IntegerField(default=100, verbose_name='Total number of steps')),
            ],
        ),
        migrations.CreateModel(
            name='VideoCloudinary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(blank=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to=video.models.user_directory_path, validators=[cloudinary_storage.validators.validate_video])),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_estimated', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
