from django.urls import path
from . import views  # Import views correctly

urlpatterns = [
    path('add/', views.add_product, name='add_product'),  # Example endpoint
]
