# Generated by Django 5.1.2 on 2024-11-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Nairobi', max_length=255),
        ),
    ]
