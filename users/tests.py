from django.test import TestCase
from django.urls import reverse, resolve
from users.views import signup, login, logout

# Create your tests here.

class UserCredsTest(TestCase):
    def test_testlogin(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)

    def test_testsign(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signup)

    def test_testout(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout)
