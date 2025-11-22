# Project Statement – Restaurant Menu Manager

## Problem Statement

Small restaurants and food outlets often rely on handwritten menus or ad-hoc spreadsheets to manage their menu items.  
This makes it difficult to quickly update prices, add new dishes, or remove discontinued items in a consistent and organized way.  
There is a need for a simple, beginner-friendly tool that allows basic menu management from a single place without requiring complex setup or databases.

## Scope of the Project

This project implements a command-line based Restaurant Menu Manager in Python.  
The system allows a user to view the complete menu, add new items, and remove existing items across multiple categories.  
The scope is intentionally limited to in-memory menu management (no database or file storage) to focus on core programming concepts like modularity, functions, and data structures.  
Advanced features such as billing, authentication, online ordering, or persistent storage are out of scope for this version and may be considered as future enhancements.

## Target Users

- Students learning Python who want a small but complete project to practice with.  
- Instructors who need a simple example of a modular Python application using multiple files.  
- Small restaurant owners or staff who want a very lightweight prototype to understand how a digital menu manager could work from the terminal.

## High-Level Features

- Categorized menu structure with four main categories:
  - Starters  
  - Main Course  
  - Desserts  
  - Drinks  

- View Menu:
  - Display all categories and their items in a neatly formatted layout.  

- Add Item:
  - Add a new dish to any category by specifying the name and price.  
  - New items are immediately visible when viewing the menu.  

- Remove Item:
  - Remove an existing dish from any category by providing its name.  
  - Name matching is done in a case-insensitive manner for convenience.  

- Modular Design:
  - Separate Python files for each category (`starters.py`, `maincourse.py`, `desserts.py`, `drinks.py`).  
  - A dedicated `inventory.py` module to aggregate and display the full menu.  
  - A `main.py` file that serves as the entry point and controls the overall user interaction loop.  

- Extensibility:
  - The code structure makes it easy to add new categories or extend functionality (e.g., updating prices, saving to files, or adding reports) in future versions.
