import starters
import maincourse
import desserts
import drinks
from inventory import show_menu

def main():
    while True:
        print("\n===== RESTAURANT MENU MANAGER =====")
        print("1. Show Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            print("\nAdd to:")
            print("1. Starters")
            print("2. Main Course")
            print("3. Desserts")
            print("4. Drinks")
            c = input("Choose category: ")

            name = input("Enter item name: ")
            price = int(input("Enter price: "))

            if c == "1":
                starters.add_starter(name, price)
            elif c == "2":
                maincourse.add_maincourse(name, price)
            elif c == "3":
                desserts.add_dessert(name, price)
            elif c == "4":
                drinks.add_drink(name, price)
            else:
                print("Invalid category")

        elif choice == "3":
            print("\nRemove from:")
            print("1. Starters")
            print("2. Main Course")
            print("3. Desserts")
            print("4. Drinks")
            c = input("Choose category: ")

            name = input("Enter item name to remove: ")

            if c == "1":
                starters.remove_starter(name)
            elif c == "2":
                maincourse.remove_maincourse(name)
            elif c == "3":
                desserts.remove_dessert(name)
            elif c == "4":
                drinks.remove_drink(name)
            else:
                print("Invalid category")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
