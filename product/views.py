from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def add_product(request):
    return JsonResponse({"message": "Product added successfully"})
