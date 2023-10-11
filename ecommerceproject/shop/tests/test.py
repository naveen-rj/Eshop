from django.test import SimpleTestCase
from django.urls import reverse, resolve

from shop.views import home, prod_details


class TestUrlSlug(SimpleTestCase):
    def test_home_slug(self):
        url = reverse('products_by_category', args=['home_slug'])
        self.assertEquals(resolve(url).func, home)

    def test_product_slug(self):
        url = reverse('prod_details', args=['home_slug', 'prod_slug'])
        self.assertEquals(resolve(url).func, prod_details)
