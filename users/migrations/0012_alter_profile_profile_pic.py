# Generated by Django 4.0.6 on 2022-07-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_request_delete_kerkesat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pic'),
        ),
    ]
