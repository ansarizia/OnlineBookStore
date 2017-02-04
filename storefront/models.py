#from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    Book_Name = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Book_logo = models.CharField(max_length=250)
    Genre = models.CharField(max_length=300)

    def __str__(self):
        return self.Book_Name + '-' + self.Author






