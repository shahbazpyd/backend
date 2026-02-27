from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICE = (
        ("admin", "Admin"),
        ("student", "Student"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICE, default=None)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email