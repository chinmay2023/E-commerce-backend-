from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Category, Product, Cart
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, CartSerializer


User = get_user_model()

# ✅ Abstract Base ViewSet to avoid redundancy
class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(BaseViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# ✅ Improved Login Function
@api_view(['POST'])
@permission_classes([permissions.AllowAny])  # Allow login without authentication
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    # ✅ Authenticate user
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
        }, status=status.HTTP_200_OK)
    
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
