# Generated by Django 5.1.1 on 2024-10-31 00:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0017_tubematerials'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputsshellandtube',
            name='tube_materials',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.tubematerials'),
        ),
        migrations.AlterField(
            model_name='tubematerials',
            name='group',
            field=models.IntegerField(choices=[(1, 'GRUPO 1'), (2, 'GRUPO 2')], help_text='De acordo com tabela TEMA - RCB-4.5.2'),
        ),
    ]
