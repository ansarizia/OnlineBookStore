#from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    book_Name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    book_logo = models.CharField(max_length=250)
    book_genre = models.CharField(max_length=300)
    book_desc = models.CharField(max_length=400)
    publish_date = models.DateField()


    def __str__(self):
        return self.book_Name + '-' + self.author






