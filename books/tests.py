from django.test import TestCase
from .models import Book, Review
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import Permission
# Create your tests here.


class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@gmail.ocm",
            password="test"
        )
        cls.can_look_detail = Permission.objects.get(
            codename="pro_user")

        cls.book = Book.objects.create(
            title="My book",
            author=cls.user,
            price="24.24"
        )

        cls.review = Review.objects.create(
            review="This is excellent book!",
            author=cls.user,
            book=cls.book
        )

    def test_book_creation(self):
        self.assertEqual(f"{self.book.title}", "My book")
        self.assertEqual(f"{self.book.author.username}", "testuser")
        self.assertEqual(f"{self.book.price}", "24.24")

    def test_books_page_access_with_logged_in_user(self):
        self.client.login(email=self.user.email, password="test")
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/books.html")
        self.assertContains(response, "My book")

    def test_books_page_access_with_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/books/" %
                             reverse("account_login"))
        response = self.client.get(
            "%s?next=/books/" % reverse("account_login")
        )
        self.assertContains(response, "Login")
        self.assertTemplateUsed(response, "account/login.html")

    def test_book_detail_view_with_and_without_permissions(self):
        self.client.login(email=self.user.email, password="test")
        # without pro_user permission
        response = self.client.get(self.book.get_absolute_url())
        self.assertEqual(response.status_code, 403)

        # with pro_user permission
        self.user.user_permissions.add(self.can_look_detail)
        response = self.client.get(self.book.get_absolute_url())
        incorrect_response = self.client.get("/books/12")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(incorrect_response.status_code, 404)
        self.assertTemplateUsed(response, "books/detail.html")
        self.assertContains(response, "24.24")
        self.assertContains(response, "his is excellent book!")

    def test_search_view(self):
        self.client.login(email=self.user.email, password="test")
        response = self.client.get(reverse('search_result'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/search_page.html")
