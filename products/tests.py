<<<<<<< HEAD
from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from products.models import Product


class IndexViewTestCase(TestCase):

    def test_index(self):

        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):
    fixtures = ['categories.json', 'goods.json']

    def setUp(self):
        self.product = Product.objects.all()

    def test_products(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']), list(self.product[:3]))

    def test_category(self):
        category = Product.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']), list(self.product.filter(category_id=category.id)))

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Catalog')
        self.assertTemplateUsed(response, 'products/products.html')
=======
from django.test import TestCase

# Create your tests here.
>>>>>>> de9e5cf (First commit)
