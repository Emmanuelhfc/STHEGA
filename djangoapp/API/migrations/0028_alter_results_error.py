# Generated by Django 5.1.1 on 2024-12-03 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0027_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='error',
            field=models.BooleanField(default=False),
        ),
    ]
