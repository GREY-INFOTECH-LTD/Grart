# Generated by Django 3.2.2 on 2023-04-22 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_auto_20220209_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='artwork_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
