from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from asgiref.sync import sync_to_async

# views.py (Django'da Seller ürün ekleme işlemi)
import httpx
from django.http import JsonResponse
from django.views import View
from .models import Seller

class SellerProductCreateView(View):
    async def post(self, request, seller_id):
        # Seller ID'yi alıyoruz
        seller = await sync_to_async(Seller.objects.get)(id=seller_id)

        # JSON'dan ürün bilgilerini alıyoruz
        product_data = {
            "seller_id": seller_id,
            "name": request.POST.get('name'),
            "description": request.POST.get('description'),
            "price": float(request.POST.get('price')),
            "stock": int(request.POST.get('stock')),
        }

        # FastAPI'ye asenkron istek gönderiyoruz
        async with httpx.AsyncClient() as client:
            fastapi_url = "http://127.0.0.1:8001/products/"  # FastAPI mikroservisinin URL'i
            response = await client.post(fastapi_url, json=product_data)

        # FastAPI'den gelen yanıtı işliyoruz
        if response.status_code == 200:
            return JsonResponse({"message": "Product created in FastAPI", "data": response.json()})
        else:
            return JsonResponse({"error": "Failed to create product in FastAPI"}, status=400)


