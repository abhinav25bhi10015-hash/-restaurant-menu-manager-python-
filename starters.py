starters = [
    {"name": "Tomato Soup", "price": 120},
    {"name": "Spring Rolls", "price": 150},
]

def add_starter(name, price):
    starters.append({"name": name, "price": price})

def remove_starter(name):
    global starters
    starters = [item for item in starters if item["name"].lower() != name.lower()]
