# Generated by Django 4.2 on 2023-05-22 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app_hotel_app', '0004_rename_name_reservations_fname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservations',
            old_name='CheckOutDate',
            new_name='check_in_date',
        ),
        migrations.RenameField(
            model_name='reservations',
            old_name='checkInDate',
            new_name='check_out_date',
        ),
        migrations.RenameField(
            model_name='reservations',
            old_name='fname',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='reservations',
            old_name='roomType',
            new_name='room_type',
        ),
    ]
