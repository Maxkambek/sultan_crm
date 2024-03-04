import uuid
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import datetime


class Branch(models.Model):
    name = models.CharField(max_length=223)
    address = models.CharField(max_length=223)
    phone = models.CharField(max_length=20)
    second_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.user_branch.all().count()

    @property
    def get_head_name(self):
        qs = self.user_branch.all()
        qs = qs.filter(role='HeadBranch').first()
        return qs.name


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise TypeError('Invalid phone number')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        ('Operator', 'Operator'),
        ('HeadBranch', 'HeadBranch'),
        ('Visa', 'Visa'),
        ('Boss', 'Boss'),
        ('SuperAdmin', 'SuperAdmin')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=19, unique=True)
    name = models.CharField(max_length=233)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    role = models.CharField(choices=ROLE, max_length=20, default='Operator')
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_branch')
    created_at = models.DateField(auto_now_add=True, null=True)
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)

    objects = AccountManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone

    @property
    def get_branch_name(self):
        return self.branch.name

    @property
    def count_clients(self):
        count = 0
        cost = 0
        qs = self.client_owner.all()
        for i in qs:
            if i.date_added.month == datetime.datetime.now().month:
                count += 1
                cost += i.price
        return {'count': count, 'cost': cost}


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.question
