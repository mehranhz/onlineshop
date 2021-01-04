from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """manager for users"""

    def create_user(self, phone, name, password=None):
        if not phone:
            raise ValueError("user must have an email address")
        phone = phone
        user = self.model(phone=phone, name=name)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, phone, name, password):
        user = self.create_user(phone, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    phone = models.CharField(max_length=13, null=True, unique=True)
    type = models.CharField(max_length=256, null=True)
    membershipDate = models.DateField(null=True)
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return "name : " + self.name +" "+ '\n  phone : ' + self.phone


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField,


class UserProfileSetting:
    def __init__(self):
        self.fields = []

    def active_fields(self, fields):
        self.fields = fields

    def __str__(self):
        return "-".join(self.fields)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.TextField()
    phone_number = models.CharField(max_length=9)
    location = models.CharField(max_length=256, null=True)
    receiver = models.CharField(max_length=256)


class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.CharField(max_length=128)
