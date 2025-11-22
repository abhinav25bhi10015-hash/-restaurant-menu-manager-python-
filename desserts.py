desserts = [
    {"name": "Gulab Jamun", "price": 100},
    {"name": "Ice Cream", "price": 90},
]

def add_dessert(name, price):
    desserts.append({"name": name, "price": price})

def remove_dessert(name):
    global desserts
    desserts = [item for item in desserts if item["name"].lower() != name.lower()]
