# Generated by Django 2.2 on 2021-02-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0011_remove_rent_id_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='top_speed',
            field=models.CharField(default='260', max_length=250),
        ),
        migrations.AddField(
            model_name='cars',
            name='transmission',
            field=models.CharField(default='Automatic', max_length=250),
        ),
    ]
