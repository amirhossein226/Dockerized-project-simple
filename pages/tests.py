from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView
# Create your tests here.


class HomePageTest(SimpleTestCase):
    def setUp(self):
        self.response = self.client.get(reverse("home"))

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_with_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template_is_correct(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_home_content_is_correct(self):
        self.assertContains(self.response, "This page is Hooooome!")

    def test_home_page_is_not_contain_incorrect_contents(self):
        self.assertNotContains(
            self.response, "Hello this is incorrect message!")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_about_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "about.html")
        self.assertContains(self.response, "This is about page!")

    def test_about_url_resolves_about_view(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
