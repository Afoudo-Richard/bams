# Generated by Django 4.0.4 on 2022-06-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_rename_travelschedule_trip_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='schedule',
            new_name='trip',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Terminated', 'Terminated')], max_length=200, null=True),
        ),
    ]
