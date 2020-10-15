# Generated by Django 3.1.2 on 2020-10-12 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_sighting_uniquesid'),
    ]

    operations = [
        migrations.CreateModel(
            name='sightingshowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sighting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.sighting')),
            ],
        ),
    ]