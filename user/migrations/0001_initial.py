# Generated by Django 5.0.3 on 2024-03-16 11:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(max_length=50, verbose_name='')),
                ('password', models.CharField(max_length=50, verbose_name='')),
                ('name', models.CharField(max_length=50, verbose_name='')),
                ('phone', models.CharField(max_length=20, verbose_name='')),
                ('address', models.CharField(max_length=200, verbose_name='')),
                ('city', models.CharField(max_length=20, verbose_name='')),
                ('country', models.CharField(max_length=20, verbose_name='')),
                ('email', models.EmailField(max_length=254, verbose_name='')),
                ('image', models.ImageField(default='images/users/default.jpg', upload_to='images/users/', verbose_name='')),
            ],
        ),
    ]
