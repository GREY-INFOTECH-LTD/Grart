# Generated by Django 3.2.2 on 2023-08-10 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20230810_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='shop_description',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='shop_name',
        ),
    ]
