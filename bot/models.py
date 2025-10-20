from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Notification(models.Model):
    EVENT_CHOICES = [('REG','Registration'),('FRAN','Franchise'),('WD','Withdrawal'),('FRAUD','Fraud')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    def __str__(self): return f"{self.event_type} - {self.user.username if self.user else 'System'}"
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kyc_id = models.CharField(max_length=128, unique=True, null=True, blank=True)
    referral_count = models.PositiveIntegerField(default=0)
    wallet_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fraud_flag = models.BooleanField(default=False)
