# Generated by Django 5.1.1 on 2024-12-03 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0029_results_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputsshellandtube',
            name='perda_carga_admissivel_casco',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inputsshellandtube',
            name='perda_carga_admissivel_tubo',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
