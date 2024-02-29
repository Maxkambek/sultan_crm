from django.contrib import admin
from .models import Client, TourPaket

admin.site.register(Client)


@admin.register(TourPaket)
class TourPaketAdmin(admin.ModelAdmin):
    pass
