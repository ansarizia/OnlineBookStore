from django.http import Http404
from django.shortcuts import render
from .models import Books
# Create your views here.

def index(request):
    all_books = Books.objects.all()
    context = {'all_books' : all_books}
    return render(request,'StoreFront/home.html',context)

def BuyNow(request, Book_id):
    try:
        book = Books.objects.get(pk=Book_id)
    except Books.DoesNotExist:
        raise Http404("Book is not available")
    context = {'book' : book}
    return render(request,'StoreFront/BuyNow.html',context)

def display_books():
    pass