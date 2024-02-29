from rest_framework import serializers
from .models import Branch, TourPaket, Client, Meeting


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'phone', 'address', 'get_count', 'get_head_name']


class TourPaketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPaket
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'owner', 'full_name', 'phone', 'date_added', 'passport_seria', 'passport_file', 'visa_file',
                  'updated_at', 'last_updater', 'paket', 'payment_taken', 'date_payment', 'status',
                  'percentage_of_payment', 'stay', 'country', 'branch_name', 'price', 'get_paket_name', 'passport_date',
                  'passport_expire']


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id', 'owner', 'date', 'description', 'branch', 'created_at', 'client_name', 'client_phone']
