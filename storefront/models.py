#from __future__ import unicode_literals

from django.db import models

class Genres(models.Model):
    genre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name

class Languages(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return  self.language

class Books(models.Model):
    book_Name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    book_logo = models.CharField(max_length=250)
    book_genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    book_language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    # book_language = models.CharField(max_length=200, default="English")
    book_desc = models.CharField(max_length=400)
    publish_date = models.DateField()
    book_price = models.CharField(max_length=20, default="100")


    def __str__(self):
        return self.book_Name + '-' + self.author










