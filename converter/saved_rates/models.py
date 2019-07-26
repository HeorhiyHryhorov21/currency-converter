from django.db import models

# Create your models here.
class Rates(models.Model):
    class Meta:
        db_table = 'rates'

    user_id = models.CharField(max_length=200)
    body = models.TextField()