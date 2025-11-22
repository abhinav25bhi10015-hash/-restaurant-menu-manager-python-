import starters
import maincourse
import desserts
import drinks

CATEGORIES = {
    "Starters": starters.starters,
    "Main Course": maincourse.maincourse,
    "Desserts": desserts.desserts,
    "Drinks": drinks.drinks,
}

def show_menu():
    print("\n============= MENU =============")
    for category, items in CATEGORIES.items():
        print(f"\n--- {category} ---")
        for item in items:
            print(f"{item['name']} - ₹{item['price']}")
    print("================================\n")
