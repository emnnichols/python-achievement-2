# Generated by Django 4.2.15 on 2024-08-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='notes',
            field=models.TextField(default='no notes...'),
        ),
    ]
