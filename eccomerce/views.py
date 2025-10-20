from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from django.shortcuts import get_object_or_404
class ProductListAPIView(APIView):
    def get(self, request):
        qs = Product.objects.filter(stock__gt=0)
        data = [{'id':p.id,'name':p.name,'price':float(p.price)} for p in qs]
        return Response(data)
class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        p = get_object_or_404(Product, pk=pk)
        return Response({'id':p.id,'name':p.name,'price':float(p.price),'stock':p.stock})
