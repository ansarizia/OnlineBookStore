from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=32)
    book_desc = models.TextField(max_length=200)
    author = models.CharField(max_length=32)
    publish_year = models.DateField
    category = models.CharField(max_length=16)

    def __str__(self):
        return "%s" % self.book_name

