# Generated by Django 3.2.2 on 2023-05-20 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_profile_artwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='artwork',
        ),
    ]
