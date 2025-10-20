from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class FortuneWheelConfig(models.Model):
    win_percentage = models.FloatField(default=30.0)
    company_commission_percentage = models.FloatField(default=20.0)
class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
class UserSpinHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_win = models.BooleanField(default=False)
    won_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    mode = models.CharField(max_length=20, default='pay_per_spin')
    spun_at = models.DateTimeField(auto_now_add=True)
