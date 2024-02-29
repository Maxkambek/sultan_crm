from django.contrib import admin
from .models import Account, Branch


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass
