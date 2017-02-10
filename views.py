from django.shortcuts import get_object_or_404,render,redirect
from .models import Books,Genres,Cart,BookOrder
from django.views import generic
# Create your Genericviews here.

def index(request):
    all_books = Books.objects.all()
    context = {'all_books' : all_books,}
    return render(request,'StoreFront/home.html',context)

def BuyNow(request, Book_id):
    book = get_object_or_404(Books, id=Book_id)
    context = {'book' : Books.objects.get(pk=Book_id),'all_books' : Books.objects.all(),'similar_genre' : Books.objects.filter(book_genre=book.book_genre)}
    return render(request,'StoreFront/BuyNow.html',context)

def Details(request,Genre):
    genre_book = Genres.objects.get(genre_name=Genre)
    genres_book = genre_book.books_set.all()
    return render(request,'StoreFront/Genres.html',{'genres_book' : genres_book})

def add_to_cart(request,book_id):
    if request.user.is_authenticated():
        try:
            book = Books.objects.get(pk=book_id)
        except Books.DoesNotExist:
            pass
        else:
            try:
                cart = Cart.objects.get(user=request.user,active=True)
            except Cart.DoesNotExist:
                cart = Cart.objects.create(user=request.user)
                cart.save()
            cart.add_to_cart(book_id)
        return redirect('cart')
    return redirect('index')


def remove_from_cart(request,book_id):
    if request.user.is_authenticated():
        try:
            book = Books.objects.get(pk=book_id)
        except Books.DoesNotExist:
            pass
        else:
            cart = Cart.objects.get(user=request.user,active=True)
            cart.remove_from_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index')


def cart(request):
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user.id,active=True)
        orders = BookOrder.objects.filter(cart=cart)
        total = 0
        count = 0
        for order in orders:
            total += (100 * order.quantity)
            count += order.quantity
        context = {
            'cart': orders,
            'total': total,
            'count': count,
        }
        return render(request,'StoreFront/cart.html',context)
    else:
        return redirect('index')










