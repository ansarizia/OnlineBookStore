from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    book_genre = models.ForeignKey(Genres)
    book_language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    # book_language = models.CharField(max_length=200, default="English")
    book_desc = models.CharField(max_length=400,default="Description")
    publish_date = models.DateField(default=timezone.now())
    book_price = models.CharField(max_length=20, default="100")


    def __str__(self):
        return self.book_Name + '-' + self.author

class Cart(models.Model):
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100,null=True)
    payment_id = models.CharField(max_length=100,null=True)

    def add_to_cart(self,book_id):
        book = Books.objects.get(pk=book_id)
        try:
            pre_existing_order =BookOrder.objects.get(book=book, cart= self)
            pre_existing_order.quantity += 1
            pre_existing_order.save()
        except BookOrder.DoesNotExist:
            new_order = BookOrder.objects.create(book=book,cart=self,quantity=1)
            new_order.save()

    def remove_from_cart(self,book_id):
        book = Books.objects.get(pk=book_id)
        try:
            pre_existing_order = BookOrder.objects.get(book=book,cart=self)
            if pre_existing_order.quantity > 1:
                pre_existing_order.quantity -= 1
                pre_existing_order.save()
        except BookOrder.DoesNotExist:
            return "There is no such book in your cart"


class BookOrder(models.Model):
    book = models.ForeignKey(Books)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField(default=0)















