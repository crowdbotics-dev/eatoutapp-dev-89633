from django.conf import settings
from django.db import models
class TestModel(models.Model):
    'Generated Model'
    years_of_experience = models.IntegerField()
