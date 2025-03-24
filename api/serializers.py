from rest_framework import serializers
from .models import ContactForm, ReservationForm, OrderForm


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'


class ReservationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationForm
        fields = '__all__'


class OrderFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderForm
        fields = '__all__'
