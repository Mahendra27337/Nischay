from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InvestmentPlan, Investment
from django.shortcuts import get_object_or_404
from decimal import Decimal
class PlansAPIView(APIView):
    def get(self, request):
        plans = InvestmentPlan.objects.all()
        return Response([{'id':p.id,'name':p.name,'tenure':p.tenure_days,'roi':float(p.roi_percent)} for p in plans])
class InvestAPIView(APIView):
    def post(self, request):
        user = request.user
        plan_id = request.data.get('plan_id')
        amount = Decimal(request.data.get('amount',0))
        plan = get_object_or_404(InvestmentPlan, pk=plan_id)
        inv = Investment.objects.create(user=user, plan=plan, amount=amount)
        return Response({'message':'investment created','id':inv.id})
