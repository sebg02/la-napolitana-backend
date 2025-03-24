from django.urls import path
from .views import ContactFormView, ReservationFormView, OrderFormView

urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact-form'),
    path('reservation/', ReservationFormView.as_view(), name='reservation-form'),
    path('order/', OrderFormView.as_view(), name='order-form'),
]
