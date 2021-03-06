from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successfull"""

        email = "jain.mohit27@gmail.com"
        password = "password123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )