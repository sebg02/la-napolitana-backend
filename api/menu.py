products = {
    "pizza_margarita": {"price": 25000, "name": "Pizza Margarita"},
    "pizza_hawaiana": {"price": 28000, "name": "Pizza Hawaiana"},
    "pizza_pepperoni": {"price": 30000, "name": "Pizza Pepperoni"},
    "pizza_vegetariana": {"price": 28000, "name": "Pizza Vegetariana"},
    "pizza_cuatro_quesos": {"price": 32000, "name": "Pizza Cuatro Quesos"},
    "pizza_carne": {"price": 30000, "name": "Pizza Carne"},
    "pizza_pollo_bbq": {"price": 30000, "name": "Pizza Pollo BBQ"},
    "pizza_mexicana": {"price": 32000, "name": "Pizza Mexicana"},
    "lasagna_carne": {"price": 26000, "name": "Lasaña de Carne"},
    "lasagna_pollo": {"price": 26000, "name": "Lasaña de Pollo"},
    "lasagna_verduras": {"price": 25000, "name": "Lasaña de Verduras"},
    "lasagna_espinacas": {"price": 26000, "name": "Lasaña de Espinacas"},
    "spaghetti_bolognesa": {"price": 22000, "name": "Spaghetti Bolognesa"},
    "spaghetti_carbonara": {"price": 23000, "name": "Spaghetti Carbonara"},
    "penne_alfredo": {"price": 24000, "name": "Penne Alfredo"},
    "penne_arrabiata": {"price": 23000, "name": "Penne Arrabiata"},
    "fettuccine_primavera": {"price": 25000, "name": "Fettuccine Primavera"},
    "bebida_gaseosa": {"price": 4000, "name": "Bebida Gaseosa (350 ml)"},
    "bebida_agua_mineral": {"price": 3000, "name": "Bebida Agua Mineral (500 ml)"},
    "bebida_jugos_naturales": {"price": 5000, "name": "Bebida Jugos Naturales"},
}


def dots_for_number(num):
    return "{:,}".format(num).replace(',', '.')


def format_order_html(raw_order) -> str:
    """
    Converts given order with products into an html format to share in an email.
    """
    html = "<ul> \n"
    total = 0
    for product in raw_order:
        if product in products:
            name = products[product]["name"]
            quantity = raw_order[product]
            price = products[product]["price"]
            subtotal = quantity * price
            total += subtotal
            li = f"<li>{quantity} x {name} ${dots_for_number(price)}(c/u) = ${dots_for_number(subtotal)} </li> \n"
            html += li
    total_string = f"<b> Total: ${dots_for_number(total)} </b> \n"
    html += "</ul>"
    html += total_string
    return html


def format_order(raw_order):
    """
    Converts given order with products and quantity into a more detailed order 
    receipt with contrasted data from backend such as prices
    """
    order = {}
    total = 0
    counter = 0
    for product in raw_order:
        if product in products:
            counter += 1
            key = f"product_{counter}"
            name = products[product]["name"]
            quantity = raw_order[product]
            price = products[product]["price"]
            subtotal = quantity * price
            total += subtotal
            data = {"name": name, "price": price,
                    "quantity": quantity, "subtotal": subtotal}

            order[key] = data

    dict_total = total
    order["total"] = dict_total
    return order
