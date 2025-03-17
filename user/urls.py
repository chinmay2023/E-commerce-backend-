from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CategoryViewSet, ProductViewSet, CartViewSet, login  # Ensure 'login' is imported

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)

urlpatterns = [
    path('login/', login, name='login'),  # Ensure login view is correct
]

urlpatterns += router.urls  # Add router-generated URLs
