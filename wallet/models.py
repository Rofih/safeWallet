import uuid
from decimal import Decimal
from email.policy import default
from uuid import uuid4

from django.conf import settings
from django.db import models

# Create your models here.

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    account_number = models.CharField(max_length=11, unique=True)



    def deposit(self, amount):
        if amount > Decimal('0.00'):
            self.balance += Decimal(amount)



class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('D','Deposit'),
        ('W','Withdraw'),
        ('T','Transfer'),
    ]
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    reference_number = models.UUIDField(max_length=40 ,unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE, default='D')
    transaction_time = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)