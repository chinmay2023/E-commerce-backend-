from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
\
class User(AbstractUser):
    email = models.EmailField(unique=True)  # Keep email for uniqueness

    USERNAME_FIELD = 'username'  # Use username as the primary login field
    REQUIRED_FIELDS = ['email']  # Email is required when creating superusers

    def __str__(self):
        return self.username


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return f"{self.name} - {self.price}"

# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_entries")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.email} - {self.product.name} x {self.quantity}"
