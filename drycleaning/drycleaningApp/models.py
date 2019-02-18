from django.db import models
from django.utils import timezone


# Create your models here.
plan = (
    ('','Choose your plan'),
    ('premium', 'Premium Plan (₦1000 - ₦5000)'),
    ('ulimate','Ultimate Plan (₦6000 - Above)'),
)

class Message(models.Model):
    phone = models.IntegerField()
    plan_type = models.CharField(max_length=30, choices=plan)
    text = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author
