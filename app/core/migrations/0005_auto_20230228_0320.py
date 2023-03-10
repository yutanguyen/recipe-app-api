# Generated by Django 3.2.18 on 2023-02-28 03:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230220_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recipe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
