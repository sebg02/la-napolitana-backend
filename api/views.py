from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ContactFormSerializer, ReservationFormSerializer, OrderFormSerializer
from .utils import send_contact_email, send_reservation_email, send_order_email
from .menu import format_order, format_order_html


class ContactFormView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            name = request.data.get("name")
            message = request.data.get("message")
            email = request.data.get("email")
            send_contact_email(name, message, email)

            return Response({"message": "Contact form submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationFormView(APIView):
    def post(self, request):
        serializer = ReservationFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            name = request.data.get("name")
            email = request.data.get("email")
            date = request.data.get("date")
            hour = request.data.get("time")
            size_group = request.data.get("size_group")
            notes = request.data.get("notes")
            send_reservation_email(name, email, date, hour, size_group, notes)

            return Response({"message": "Reservation submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderFormView(APIView):
    def post(self, request):
        data = request.data.copy()
        data["products"] = format_order(data["products"])

        serializer = OrderFormSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            name = request.data.get("full_name")
            email = request.data.get("email")
            address = request.data.get("address")
            notes = request.data.get("notes")
            order = format_order_html(request.data.get("products"))
            send_order_email(name, email, address, notes, order)

            return Response({"message": "Order submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
