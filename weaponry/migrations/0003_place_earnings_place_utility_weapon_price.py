# Generated by Django 5.1.1 on 2024-11-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weaponry', '0002_place_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='earnings',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='place',
            name='utility',
            field=models.CharField(choices=[('repair', 'Repair'), ('sell', 'Sell'), ('No utility', 'No utility')], default='No utility', max_length=100),
        ),
        migrations.AddField(
            model_name='weapon',
            name='price',
            field=models.FloatField(default=100),
        ),
    ]
