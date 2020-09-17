from django.views.generic import ListView
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from .models import Book


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>Class View Demo </h1>')


class HelloView(TemplateView):
    template_name = 'hello.html'


class ListBooksView(ListView):
    model = Book
    # default context name is object_list
    # default template is  templates/books/book_list.html
    context_object_name = 'books'  # name to be sent to template
