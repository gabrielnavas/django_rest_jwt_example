from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    pages = models.IntegerField(null=False)
