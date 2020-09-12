
from django.urls import path
from . import views, class_views
from .rest import rest_views

urlpatterns = [
    path('home/', views.book_home),
    path('list/', views.book_list),
    path('add/', views.book_add),
    path('delete/<int:id>', views.book_delete),
    path('edit/<int:id>', views.book_edit),
    path('search/', views.book_search),
    path('dosearch/', views.book_do_search),

    # Class based views
    path("hello/", class_views.HelloView.as_view()),
    path("listbooks/", class_views.ListBooksView.as_view()),

    # REST API views
    path('rest/books/', rest_views.process_books),
    path('rest/books/<int:id>', rest_views.process_one_book),

]
