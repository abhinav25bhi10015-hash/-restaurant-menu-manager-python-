# Restaurant Menu Manager

A simple command-line Restaurant Menu Manager written in Python.  
This project lets you manage a restaurant menu with four categories: Starters, Main Course, Desserts, and Drinks. You can view the full menu, add new items, and remove existing items directly from the terminal.

---

## Features

- View a neatly formatted menu with all categories and items.
- Add new dishes with a name and price to any category.
- Remove dishes by name from any category (case-insensitive).
- Modular code split across multiple Python files for better structure and readability.

---

## Project Structure

- `main.py` – Entry point; shows the main menu and handles user input.
- `inventory.py` – Collects all categories and prints the complete menu.
- `starters.py` – Stores starter items and functions to add/remove starters.
- `maincourse.py` – Stores main course items and functions to add/remove them.
- `desserts.py` – Stores dessert items and functions to add/remove them.
- `drinks.py` – Stores drink items and functions to add/remove them.

---

## Requirements

- Python 3.x installed on your system.

No external libraries are required; this project only uses Python’s standard library.

---

## How to Run

1. Clone the repository:
2. Run the main script:
3. Use the on-screen menu:

- `1` → Show full menu  
- `2` → Add an item  
- `3` → Remove an item  
- `4` → Exit  

---

## Learning Goals

This project is great for practicing:

- Working with lists and dictionaries.
- Writing and using functions.
- Splitting code into multiple modules and importing them.
- Building a simple text-based user interface with `input()` and `print()`.

---

## Future Improvements

Some ideas to extend this project:

- Save and load menu items from a file (so changes persist).
- Add input validation and error handling.
- Add an option to update the price of an existing item.
- Convert it into a GUI or web-based application in the future.

---

## License

This project is for learning purposes. You can modify and use it as you like.
