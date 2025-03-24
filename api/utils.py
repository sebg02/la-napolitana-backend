import requests
import os
import environ
# from django.conf import settings


EMAILJS_USER_ID=os.environ.get("EMAILJS_USER_ID")
EMAILJS_SERVICE_ID=os.environ.get("EMAILJS_SERVICE_ID")
EMAILJS_PK=os.environ.get("EMAILJS_PK")
EMAILJS_PK_ORDER =os.environ.get("EMAILJS_PK_ORDER")
EMAILJS_USER_ORDER_ID=os.environ.get("EMAILJS_USER_ORDER_ID")
EMAILJS_SERVICE_ORDER_ID=os.environ.get("EMAILJS_SERVICE_ORDER_ID")
EMAILJS_TEMPLATE_CONTACT_ID=os.environ.get("EMAILJS_TEMPLATE_CONTACT_ID")
EMAILJS_TEMPLATE_RESERVATION_ID=os.environ.get("EMAILJS_TEMPLATE_RESERVATION_ID")
EMAILJS_TEMPLATE_ORDER_ID=os.environ.get("EMAILJS_TEMPLATE_ORDER_ID")
EMAILJS_API_URL=os.environ.get("EMAILJS_API_URL")


def send_contact_email(name, message, email):
    email_data = {
        "service_id": EMAILJS_SERVICE_ID,
        "template_id": EMAILJS_TEMPLATE_CONTACT_ID,
        "user_id": EMAILJS_USER_ID,
        "template_params": {
            "name":name,
            "message":message,
            "email":email,
        },
        "accessToken": EMAILJS_PK,
    }

    response = requests.post(EMAILJS_API_URL, json=email_data)
    print("EmailJS Status Code:", response.status_code)
    print("EmailJS Response:", response.text)
    return response.status_code == 200  


def send_reservation_email(name, email, date, hour, size_group, notes):
    email_data = {
        "service_id": EMAILJS_SERVICE_ID,
        "template_id": EMAILJS_TEMPLATE_RESERVATION_ID,
        "user_id": EMAILJS_USER_ID,
        "template_params": {
            "name":name,
            "email":email,
            "date":date,
            "hour":hour,
            "size_group":size_group,
            "notes":notes,
        },
        "accessToken": EMAILJS_PK,
    }

    response = requests.post(EMAILJS_API_URL, json=email_data)
    print("EmailJS Status Code:", response.status_code)
    print("EmailJS Response:", response.text)
    return response.status_code == 200


def send_order_email(name, email, address, notes, order):
    email_data = {
        "service_id": EMAILJS_SERVICE_ORDER_ID,
        "template_id": EMAILJS_TEMPLATE_ORDER_ID,
        "user_id": EMAILJS_USER_ORDER_ID,
        "template_params": {
            "name":name,
            "email":email,
            "address":address,
            "notes":notes,
            "order":order,
        },
        "accessToken": EMAILJS_PK_ORDER,
    }

    response = requests.post(EMAILJS_API_URL, json=email_data)
    print("EmailJS Status Code:", response.status_code)
    print("EmailJS Response:", response.text)
    return response.status_code == 200






 