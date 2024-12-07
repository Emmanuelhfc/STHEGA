# Generated by Django 5.1.1 on 2024-12-04 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0031_alter_inputsshellandtube_perda_carga_admissivel_casco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputsshellandtube',
            name='ls_percent',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='Espaçamento entre defletores em funçao do diametro interno do trocador (Ds) (%)', max_digits=4, null=True),
        ),
    ]
