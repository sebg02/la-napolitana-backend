from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()


class ReservationForm(models.Model):
    date = models.DateField()
    time = models.TimeField()
    size_group = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)


class OrderForm(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    notes = models.TextField(blank=True, null=True)
    products = models.JSONField()
