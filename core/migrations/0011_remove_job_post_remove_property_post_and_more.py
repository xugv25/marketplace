# Generated by Django 4.1.7 on 2023-06-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_car_job_property_remove_post_category_post_post_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='post',
        ),
        migrations.RemoveField(
            model_name='property',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_type',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='car ', max_length=50),
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
