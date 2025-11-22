maincourse = [
    {"name": "Paneer Butter Masala", "price": 250},
    {"name": "Veg Biryani", "price": 220},
]

def add_maincourse(name, price):
    maincourse.append({"name": name, "price": price})

def remove_maincourse(name):
    global maincourse
    maincourse = [item for item in maincourse if item["name"].lower() != name.lower()]
