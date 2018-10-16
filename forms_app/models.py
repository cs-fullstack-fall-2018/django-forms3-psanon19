from django.db import models
from datetime import datetime


class FormModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    operating_budget = models.IntegerField(default=0)
    description = models.TextField(null=True, max_length=500)
    number_of_employees = models.IntegerField(default=0)
    established_date = models.DateTimeField(default=datetime.now)
    image_url = models.URLField(null=True, max_length=500)

    def __str__(self):
        return self.name
