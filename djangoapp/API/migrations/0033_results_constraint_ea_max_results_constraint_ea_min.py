# Generated by Django 5.1.1 on 2024-12-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0032_alter_inputsshellandtube_ls_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='constraint_ea_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='constraint_ea_min',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
