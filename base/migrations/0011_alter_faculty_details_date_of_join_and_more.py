# Generated by Django 4.1.4 on 2023-01-15 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_faculty_details_date_of_join_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_details',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 1, 15, 20, 25, 33, 621991)),
        ),
        migrations.AlterField(
            model_name='faculty_details',
            name='image',
            field=models.ImageField(default='images/Screenshot_3.png', upload_to='photo/%Y/%m/%d'),
        ),
    ]