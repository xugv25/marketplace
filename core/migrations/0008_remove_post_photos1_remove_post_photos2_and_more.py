# Generated by Django 4.1.7 on 2023-06-07 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_post_photos4_post_photos5'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photos1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photos2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photos3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photos5',
        ),
    ]