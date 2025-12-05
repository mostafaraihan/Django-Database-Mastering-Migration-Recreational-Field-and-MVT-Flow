import uuid

from django.db import models


class Demo_Col(models.Model):
    col1 = models.CharField()  # ***
    col2 = models.CharField(max_length=100)
    col3 = models.TextField()  # ***
    col4 = models.IntegerField()  # ***
    col5 = models.BigIntegerField()  # ***
    col6 = models.SmallIntegerField()
    col7 = models.FloatField()  # ***
    col8 = models.DecimalField(max_digits=5, decimal_places=2)
    col9 = models.SlugField(max_length=100)
    col10 = models.EmailField(max_length=100)  # ***
    col11 = models.URLField(max_length=100)  # ***
    col12 = models.UUIDField(default=uuid.uuid4)  # ***
    col13 = models.BooleanField(default=True)  # ***
    col14 = models.DateField(auto_now_add=True)  # ***
    col15 = models.TimeField(auto_now_add=True)
    col16 = models.DateTimeField(auto_now_add=True)  # ***
    col17 = models.DurationField()
    col18 = models.BinaryField()
