# Generated by Django 5.1.1 on 2024-10-30 23:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0013_rename_tube_thickness_incb_tubeinterndiameter_tube_thickness_inch'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputsshellandtube',
            name='ls',
            field=models.DecimalField(decimal_places=1, help_text='Espaçamento entre defletores em funçao do comprimento (L) do trocador', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
