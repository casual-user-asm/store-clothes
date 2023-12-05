from django.db import models
<<<<<<< HEAD
import stripe
from django.conf import settings
from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY
=======

from users.models import User
>>>>>>> de9e5cf (First commit)


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    descriprtion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    descriprtion = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
<<<<<<< HEAD
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True)
=======
>>>>>>> de9e5cf (First commit)
    image = models.ImageField(upload_to='products_images')
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return f'Product: {self.name} | Category {self.category}'

<<<<<<< HEAD
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.stripe_product_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_price['id']
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'], unit_amount=round(self.price * 100), currency='usd'
        )
        return stripe_product_price

=======
>>>>>>> de9e5cf (First commit)

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
<<<<<<< HEAD

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def stripe_products(self):
        line_items = []
        for basket in self:
            item = {
                'price': basket.product.stripe_product_price_id,
                'quantity': basket.quantity,
            }
            line_items.append(item)
        return line_items

=======
    
    def total_quantity(self):
        return sum(basket.quantity for basket in self)

>>>>>>> de9e5cf (First commit)

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self) -> str:
        return f'{self.user.username} | {self.product.name}'
<<<<<<< HEAD

    def sum(self):
        return self.quantity * self.product.price

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return basket_item
=======
    
    def sum(self):
        return self.quantity * self.product.price
>>>>>>> de9e5cf (First commit)
