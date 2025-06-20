# Generated by Django 5.1.6 on 2025-02-20 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0003_truck_tracker_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_latitude', models.FloatField(blank=True, null=True)),
                ('last_longitude', models.FloatField(blank=True, null=True)),
                ('speed', models.FloatField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('truck', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tracker', to='booking.truck')),
            ],
        ),
        migrations.CreateModel(
            name='TrackingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('speed', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tracker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='tracker.tracker')),
            ],
        ),
    ]
