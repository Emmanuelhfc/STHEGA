# Generated by Django 5.1.1 on 2024-11-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0023_rename_pression_class_inputsshellandtube_pressure_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layout',
            name='name',
            field=models.CharField(choices=[('triangular', 'Triangular'), ('rotated', 'Rotated'), ('square', 'Square')], max_length=256),
        ),
    ]
