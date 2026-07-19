"""
File: app.py
Author: Janet Portillo (Jport-GH)
Date: 2026-06-25
Purpose:
    Provides the menu system and user interaction for the VSP Acronym Assistant.
    Uses modular functions to reduce deep nesting and improve readability.
Resources:
    No starter code used. Created for CSCI 1151 Project 8–11.
"""

from acronym_manager import AcronymManager


class AcronymApp:
    """
    Handles the user interface and menu loop for the application.
    Uses helper methods to avoid deep nesting and improve organization.
    """

    def __init__(self):
        """Initialize the app with an AcronymManager instance."""
        self.manager = AcronymManager()

    # ------------------------------------------------------------
    # Menu Display
    # ------------------------------------------------------------

    def display_menu(self):
        """Display the main menu options."""
        print("\n--- VSP Acronym Assistant ---")
        print("Choose an option:")
        print("  1 - Search Acronym")
        print("  2 - List by Category")
        print("  3 - Add Acronym")
        print("  4 - Save Acronyms to File")
        print("  5 - Load Acronyms from File")
        print("  6 - Quit")

    # ------------------------------------------------------------
    # Menu Option Handlers (Chapter 8–11 modularization)
    # ------------------------------------------------------------

    def handle_search(self):
        """Handle searching for an acronym."""
        short = input("Enter acronym to search: ")
        result = self.manager.search_acronym(short)
        print(result if result else "Acronym not found.")

    def handle_list_by_category(self):
        """Handle listing acronyms by category."""
        print("\nAvailable Categories:")
        categories = self.manager.get_categories()

        for i, c in enumerate(categories, start=1):
            print(f"  {i} - {c}")

        selection = input("\nEnter the number of the category: ")

        if not selection.isdigit() or not (1 <= int(selection) <= len(categories)):
            print("Invalid selection.")
            return

        category = categories[int(selection) - 1]
        results = self.manager.list_by_category(category)

        if results:
            for a in results:
                print(a)
        else:
            print("No acronyms found in that category.")

    def handle_add(self):
        """Handle adding a new acronym."""
        short = input("Enter acronym: ")
        definition = input("Enter definition: ")
        category = input("Enter category: ")
        self.manager.add_acronym(short, definition, category)
        print("Acronym added successfully.")

    def handle_save(self):
        """Handle saving acronyms to a file."""
        self.manager.save_to_file()
        print("Acronyms saved to file.")

    def handle_load(self):
        """Handle loading acronyms from a file."""
        self.manager.load_from_file()
        print("Acronyms loaded from file.")

    # ------------------------------------------------------------
    # Main Loop (now clean, no deep nesting)
    # ------------------------------------------------------------

    def run(self):
        """Run the main menu loop."""
        actions = {
            "1": self.handle_search,
            "2": self.handle_list_by_category,
            "3": self.handle_add,
            "4": self.handle_save,
            "5": self.handle_load,
            "6": self.exit_app
        }

        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please try again.")

    def exit_app(self):
        """Exit the application."""
        print("Goodbye!")
        exit()
