# Generated by Django 5.1.1 on 2024-10-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_inputsshellandtube_ds_inch'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputsshellandtube',
            name='L',
            field=models.FloatField(null=True),
        ),
    ]
