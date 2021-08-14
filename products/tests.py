from genesis_proj.views import homepage
from django.test import TestCase
from django.urls import reverse, resolve
from products.views import prod_update, prod_add


# Create your tests here.

class URLTests(TestCase):
    def test_testhomeprod(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, homepage)
    
    def test_testaddprod(self):
        url = reverse('product_add')
        print(resolve(url))
        self.assertEquals(resolve(url).func, prod_add)

    def test_testupdateprod(self):
        url = reverse('product_update',kwargs={'pk': 3})
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, prod_update)





    