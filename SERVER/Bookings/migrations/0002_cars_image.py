# Generated by Django 2.2 on 2021-01-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='image',
            field=models.ImageField(default='Media/bubble.png', upload_to='Media/images/cars'),
        ),
    ]
