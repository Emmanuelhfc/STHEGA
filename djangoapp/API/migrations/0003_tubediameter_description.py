# Generated by Django 5.1.1 on 2024-10-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_layout_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tubediameter',
            name='description',
            field=models.CharField(null=True),
        ),
    ]
