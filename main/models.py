import os

from django.db import models
from accounts.models import Account, Branch


class TourPaket(models.Model):
    TYPE = (
        ('Standard', 'Standard'),
        ('Comfort', 'Comfort'),
        ('VIP', 'VIP')
    )
    name = models.CharField(max_length=123)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date_go = models.DateField()
    date_back = models.DateField()
    duration = models.PositiveIntegerField()
    type_paket = models.CharField(max_length=123, choices=TYPE, default='Standard')
    description = models.TextField(null=True, blank=True)
    reys = models.CharField(max_length=123, null=True, blank=True)
    avia_company = models.CharField(max_length=123, null=True, blank=True)
    madina_hotel = models.CharField(max_length=123, null=True, blank=True)
    madina_duration = models.CharField(max_length=230, null=True, blank=True)
    madina_dish = models.CharField(max_length=230, null=True, blank=True)
    makka_hotel = models.CharField(max_length=123, null=True, blank=True)
    makka_duration = models.CharField(max_length=230, null=True, blank=True)
    makka_dish = models.CharField(max_length=230, null=True, blank=True)
    current_quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.paket_clients.all().count()

    @property
    def status(self):
        return self.quantity == self.current_quantity


class Client(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Active', 'Active'),
        ("SendVisa", "SendVisa"),
        ("Ready", "Ready"),
        ('Completed', 'Completed')
    )
    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name='client_owner')
    full_name = models.CharField(max_length=323)
    phone = models.CharField(max_length=22)
    date_added = models.DateTimeField(auto_now_add=True)
    passport_file = models.FileField(upload_to="passports/", null=True, blank=True)
    passport_seria = models.CharField(max_length=32, null=True, blank=True)
    passport_date = models.CharField(max_length=32, null=True, blank=True)
    passport_expire = models.CharField(max_length=32, null=True, blank=True)
    visa_file = models.FileField(upload_to='visas/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_updater = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='last_updater')
    paket = models.ForeignKey(TourPaket, on_delete=models.SET_NULL, null=True, blank=True, related_name="paket_clients")
    payment_taken = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    date_payment = models.DateField(null=True)
    status = models.CharField(max_length=123, choices=STATUS, default='New')
    stay = models.CharField(max_length=123, null=True)
    country = models.CharField(max_length=123, null=True)
    description = models.TextField(null=True, blank=True)
    residence = models.CharField(max_length=123,default="Uzbekistan")

    @property
    def percentage_of_payment(self):
        return (self.payment_taken * 100) / self.paket.price

    def __str__(self):
        return self.full_name

    @property
    def get_paket_name(self):
        return self.paket.name

    @property
    def branch_name(self):
        return self.owner.branch.name


class Meeting(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    )
    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    description = models.TextField()
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=223, null=True, blank=True)
    client_phone = models.CharField(max_length=22, null=True, blank=True)
    status = models.CharField(max_length=123, choices=STATUS_CHOICES, default='New')

    def __str__(self):
        return self.client_name


class BranchStatistics(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    paket = models.ForeignKey(TourPaket, on_delete=models.SET_NULL, null=True, blank=True)
    taken_payment = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
