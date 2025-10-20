from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class InvestmentPlan(models.Model):
    name = models.CharField(max_length=50)
    tenure_days = models.PositiveIntegerField()
    roi_percent = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self): return f"{self.name} - {self.roi_percent}%"
class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(InvestmentPlan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    matured = models.BooleanField(default=False)
