# Generated by Django 4.1.7 on 2023-06-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_post_photos1_remove_post_photos2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('car', 'A car'), ('property', 'A Property'), ('job', 'Job')], default='car', max_length=20),
        ),
    ]
