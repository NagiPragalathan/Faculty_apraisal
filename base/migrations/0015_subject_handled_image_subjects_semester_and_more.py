# Generated by Django 4.1.4 on 2023-01-16 03:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_subjects_discription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject_handled',
            name='image',
            field=models.ImageField(default='images/Screenshot_1.png', upload_to='photo/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='subjects',
            name='semester',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faculty_details',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 1, 16, 9, 27, 59, 931984)),
        ),
    ]