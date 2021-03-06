# Generated by Django 4.0.4 on 2022-05-18 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_booking_bus_driver_parcel_travelschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('account_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('account_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.accountcategory')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='booking',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.travelschedule'),
        ),
        migrations.AddField(
            model_name='travelschedule',
            name='bus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.bus'),
        ),
        migrations.AddField(
            model_name='travelschedule',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.driver'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.user'),
        ),
        migrations.AddField(
            model_name='parcel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.user'),
        ),
    ]
