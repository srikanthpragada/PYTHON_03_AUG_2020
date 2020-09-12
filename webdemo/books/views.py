from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg
from .models import Book
from django.core.exceptions import ObjectDoesNotExist
from .forms import BookForm
import datetime


def book_home(request):
    summary = Book.objects.all().aggregate(count=Count('id'),
                                           avgprice=Avg('price'))
    return render(request, 'home.html', {'summary': summary})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})


# /books/delete/10
def book_delete(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return redirect("/books/list")
    except ObjectDoesNotExist:
        return render(request, 'delete.html', {'msg': 'Book Id Not Found!'})
    except Exception as ex:
        print(ex)  # Goes to server window
        return render(request, 'delete.html', {'msg': 'Book could not be deleted!'})


def book_add(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, 'add.html', {'form': form})
    else:  # POST
        form = BookForm(request.POST)  # bind form with post data
        if form.is_valid():
            form.save()  # Add book to table
            return redirect("/books/list")
        else:
            return render(request, 'add.html', {'form': form})


# /books/edit/10
def book_edit(request, id):
    if request.method == "GET":
        try:
            book = Book.objects.get(id=id)  # Take data from DB
            form = BookForm(instance=book)
            return render(request, 'edit.html', {'form': form})
        except ObjectDoesNotExist:
            return render(request, 'edit.html', {'msg': 'Book Id Not Found!'})
    else:  # POST
        book = Book.objects.get(id=id)
        form = BookForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()  # Update
            return redirect("/books/list")
        else:
            return render(request, 'edit.html', {'form': form})


def book_search(request):
    # Use cookie search, if it is present
    if 'search' in request.COOKIES:
        title = request.COOKIES['search']
    else:
        title = ''

    return render(request, 'search.html', {'title': title})


def book_do_search(request):
    title = request.GET['title']
    # convert Book object to dict
    books = list(Book.objects.filter(title__contains=title).values())
    # send list of dict in the form of array of json objects
    resp = JsonResponse(books, safe=False)
    # Create cookie with name search and value is value of title
    resp.set_cookie("search", title,
                    expires=datetime.datetime.now() + datetime.timedelta(days=7))
    return resp
