from django.http import Http404
from django.shortcuts import render
from .models import Books
# Create your views here.

def index(request):
    all_books = Books.objects.all()
    #catalogue = Catalogue.objects.all()
    context = {'all_books' : all_books }
    return render(request,'StoreFront/home.html',context)

def BuyNow(request, Book_id):
    try:
        book = Books.objects.get(pk=Book_id)
        all_books = Books.objects.all()
    except Books.DoesNotExist:
        raise Http404("Book is not available")
    context = {'book' : book, 'all_books' : all_books}
    return render(request,'StoreFront/BuyNow.html',context)

def Details(request):
    genres_book = Books.objects.all()
    return render(request,'StoreFront/Genres.html',{'genres_book' : genres_book})




