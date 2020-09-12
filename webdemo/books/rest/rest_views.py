from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book


# To perform JSON Serialization - Book to JSON
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price')


@api_view(['GET', 'POST'])
def process_books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:  # Post
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()  # insert into table
            return Response(book.data)
        else:
            return Response(book.errors, status=400)  # bad request


@api_view(['GET', 'DELETE', 'PUT'])
def process_one_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except:
        return Response(status=404)  # not found

    if request.method == "GET":
        serializer = BookSerializer(book)  # Object to JSON
        return Response(serializer.data)
    elif request.method == "DELETE":  # DELETE
        book.delete() # Delete from Database
        return Response(status=204)  # No data
    else:  # PUT
        price = request.POST['price']
        book.price = price
        book.save()  # Update table in DB
        serializer = BookSerializer(book)
        return Response(serializer.data)

