from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from decimal import Decimal
from django.utils import timezone
from .models import FortuneWheelConfig, UserWallet, UserSpinHistory
import random
class PayPerSpinAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        spins = int(request.data.get('spins',1))
        cost = Decimal(1)*spins
        wallet, _ = UserWallet.objects.get_or_create(user=user)
        if wallet.balance < cost:
            return Response({'error':'insufficient balance'}, status=400)
        wallet.balance -= cost; wallet.save()
        results = []
        config = FortuneWheelConfig.objects.first()
        win_pct = config.win_percentage if config else 30.0
        for _ in range(spins):
            if random.uniform(0,100) <= win_pct:
                reward = Decimal(2)
                wallet.balance += reward; wallet.save()
                UserSpinHistory.objects.create(user=user,is_win=True,won_amount=reward,mode='pay_per_spin')
                results.append({'result':'win','amount':float(reward)})
            else:
                UserSpinHistory.objects.create(user=user,is_win=False,won_amount=0,mode='pay_per_spin')
                results.append({'result':'lose'})
        return Response({'results':results,'balance':float(wallet.balance)})
class DailySpinAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        wallet, _ = UserWallet.objects.get_or_create(user=user)
        bet = Decimal(10)
        if wallet.balance < bet:
            return Response({'error':'insufficient balance'}, status=400)
        wallet.balance -= bet; wallet.save()
        config = FortuneWheelConfig.objects.first()
        win_pct = config.win_percentage if config else 30.0
        if random.uniform(0,100) <= win_pct:
            reward = Decimal(20); wallet.balance += reward; wallet.save()
            UserSpinHistory.objects.create(user=user,is_win=True,won_amount=reward,mode='daily')
            return Response({'result':'win','amount':float(reward),'balance':float(wallet.balance)})
        UserSpinHistory.objects.create(user=user,is_win=False,won_amount=0,mode='daily')
        return Response({'result':'lose','balance':float(wallet.balance)})
