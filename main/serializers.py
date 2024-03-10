from rest_framework import serializers
from .models import Branch, TourPaket, Client, Meeting


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'phone', 'address', 'get_count', 'get_head_name']


class TourPaketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPaket
        fields = ['id', 'name', 'price', 'quantity', 'date_go', 'date_back', 'duration', 'type_paket', 'description',
                  'reys', 'avia_company', 'madina_duration', 'madina_hotel', 'madina_dish', 'makka_duration',
                  'makka_dish', 'makka_duration','makka_hotel' ,'current_quantity', 'get_count']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'owner', 'full_name', 'phone', 'date_added', 'passport_seria', 'passport_file', 'visa_file',
                  'updated_at', 'last_updater', 'paket', 'payment_taken', 'date_payment', 'status',
                  'percentage_of_payment', 'stay', 'country', 'branch_name', 'price', 'get_paket_name', 'passport_date',
                  'passport_expire', 'description','residence']


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id', 'owner', 'date', 'description', 'branch', 'created_at', 'client_name', 'client_phone']
