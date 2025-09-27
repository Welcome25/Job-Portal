from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('jobseeker', 'Job Seeker'),
        ('employer', 'Employer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='jobseeker')
    phone = models.CharField(max_length=15, blank=True)
    company = models.CharField(max_length=100, blank=True)  # For employers

    def __str__(self):
        return self.username
