# Generated by Django 3.1.2 on 2020-10-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='uniquesid',
            field=models.CharField(default='DL-SF-DDDD-DD', max_length=16),
        ),
    ]