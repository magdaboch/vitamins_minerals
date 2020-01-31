from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class MyUser(User):
    user_products = models.ManyToManyField(to=Product, null=True)