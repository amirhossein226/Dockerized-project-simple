from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

# Create your tests here.


UserModel = get_user_model()


class CustomUserTest(TestCase):
    def test_user_creation(self):
        user = UserModel.objects.create_user(
            username="ali", email="ali@gmail.com", password="ali1234")
        self.assertEqual(user.username, 'ali')
        self.assertEqual(user.email, 'ali@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_superuser_creation(self):
        superuser = UserModel.objects.create_superuser(
            username='amir', email="amir@gmail.com", password='amir1234')

        self.assertEqual(superuser.username, 'amir')
        self.assertEqual(superuser.email, 'amir@gmail.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)


class SignUpViewTest(TestCase):
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')

    def test_signup_form(self):
        self.assertContains(self.response, "csrfmiddlewaretoken")
