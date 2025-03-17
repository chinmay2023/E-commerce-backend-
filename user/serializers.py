from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Product, Cart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Includes all fields in the Category model

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Includes all fields in the Product model

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Nested serializer to display product details
    user = UserSerializer(read_only=True)  # Nested serializer to display user details

    class Meta:
        model = Cart
        fields = '__all__'
