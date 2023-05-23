from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Reservations(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    CHOICES = (
        ('Deluxe room', 'Deluxe room'),
        ('Standard room', 'Standard room'),
        ('Suite', 'Suite'),
        ('Family room', 'Family room'),
    )
    room_type = models.CharField(max_length=50, choices = CHOICES)
    check_in_date = models.DateField(null=True)
    check_out_date = models.DateField()

    def __str__(self):
        return self.full_name