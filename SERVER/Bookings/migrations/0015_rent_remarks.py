# Generated by Django 2.2 on 2021-02-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0014_auto_20210204_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='remarks',
            field=models.TextField(default='Returned in Perfect Condition'),
        ),
    ]
