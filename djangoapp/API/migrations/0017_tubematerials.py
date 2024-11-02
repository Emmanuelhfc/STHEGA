# Generated by Django 5.1.1 on 2024-10-30 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0016_rename_ls_inputsshellandtube_ls_percent'),
    ]

    operations = [
        migrations.CreateModel(
            name='TubeMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField(choices=[(1, 'GRUPO 1'), (2, 'GRUPO 2')])),
                ('material', models.CharField(max_length=100)),
            ],
        ),
    ]
