# Generated by Django 4.1.7 on 2023-05-30 15:51

from django.db import migrations, models
from django.conf import settings



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('marka', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]
