# Generated by Django 3.1.2 on 2020-10-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20201018_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]