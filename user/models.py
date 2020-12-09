from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """manager for users"""

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("user must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = models.BooleanField(default=True)
        user.save(using=self.db)

        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    phone = models.CharField(max_length=13, null=True)
    type = models.CharField(max_length=256, null=True)
    membershipDate = models.DateField(null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
