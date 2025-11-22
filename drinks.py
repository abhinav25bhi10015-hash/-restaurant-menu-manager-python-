drinks = [
    {"name": "Cold Coffee", "price": 120},
    {"name": "Lemonade", "price": 80},
]

def add_drink(name, price):
    drinks.append({"name": name, "price": price})

def remove_drink(name):
    global drinks
    drinks = [item for item in drinks if item["name"].lower() != name.lower()]
