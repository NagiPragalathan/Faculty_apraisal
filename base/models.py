from django.db import models

# Create your models here.


class users(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    role = models.IntegerField()