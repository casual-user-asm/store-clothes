from django.test import TestCase
<<<<<<< HEAD
from django.urls import reverse
from http import HTTPStatus


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')

    def test_user_registration(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Registration')
        self.assertTemplateUsed(response, 'users/registration.html')
=======

# Create your tests here.
>>>>>>> de9e5cf (First commit)
