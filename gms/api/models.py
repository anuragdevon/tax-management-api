import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):

    admin = 1
    tax_accountant = 2
    tax_payer = 3

    # Creating Roles
    ROLE_CHOICES = (
        (admin, 'Admin'),
        (tax_accountant, 'Tax Accountant'),
        (tax_payer, 'Tax Payer'),
    )

    # Creating User
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=tax_payer)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    objects = CustomUserManager()

    def __str__(self):
        return self.email



