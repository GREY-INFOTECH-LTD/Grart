# Generated by Django 3.2.2 on 2023-04-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0037_delete_newproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='predicted_titles',
            field=models.JSONField(blank=True, null=True),
        ),
    ]