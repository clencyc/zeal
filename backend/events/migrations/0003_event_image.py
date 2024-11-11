# Generated by Django 5.1.2 on 2024-11-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_date_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, help_text='Optional image associated with the ticket.', null=True, upload_to='events/images/'),
        ),
    ]