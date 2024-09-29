from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Book
from django.urls import reverse_lazy
from django.db.models import Q


# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/books.html"
    context_object_name = "books"
    login_url = reverse_lazy("account_login")


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = "books/detail.html"
    context_object_name = "book"
    login_url = reverse_lazy("account_login")
    permission_required = "books.pro_user"
    queryset = Book.objects.prefetch_related("reviews__author").all()


class SearchBooksView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/search_page.html'
    context_object_name = "book_list"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
