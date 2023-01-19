# Generated by Django 4.1.4 on 2023-01-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_users_mail_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200, unique=True)),
                ('subject_code', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]