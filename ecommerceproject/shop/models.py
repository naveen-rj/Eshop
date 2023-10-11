from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='category', null=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # related to context processor
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])  # 'products_by_category' from urls (slug)

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='products', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('prod_details', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
