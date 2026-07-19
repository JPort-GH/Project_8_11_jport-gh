"""
File: app.py
Author: Janet Portillo (Jport-GH)
Date: 2026-06-25
Purpose:
    Provides the menu system and user interaction for the VSP Acronym Assistant.
    This class handles input, output, and calls to the AcronymManager.
Resources:
    No starter code used. Created for CSCI 1151 Project 1.
"""
from acronym_manager import AcronymManager

class AcronymApp:
    """
    Handles the user interface and menu loop for the application.
    """

    def __init__(self):
        """Initialize the app with an AcronymManager instance."""
        self.manager = AcronymManager()

    def display_menu(self):
        """
        Display the main menu options.
        """
        print("\n--- VSP Acronym Assistant ---")
        print("Choose an option:")
        print("  1 - Search Acronym")
        print("  2 - List by Category")
        print("  3 - Add Acronym")
        print("  4 - Save Acronyms to File")
        print("  5 - Load Acronyms from File")
        print("  6 - Quit")

    def run(self):
        """
        Run the main menu loop.
        """
        while True:
            self.display_menu()
            choice = input("Enter your choice (1=Search, 2=List, 3=Add, 4=Save, 5=Load, 6=Quit): ")

            # Option 1: Search Acronym
            if choice == "1":
                short = input("Enter acronym to search: ")
                result = self.manager.search_acronym(short)
                if result:
                    print(result)
                else:
                    print("Acronym not found.")

            # Option 2: List by Category (UPDATED)
            elif choice == "2":
                print("\nAvailable Categories:")
                categories = self.manager.get_categories()

                # Display numbered list
                for i, c in enumerate(categories, start=1):
                    print(f"  {i} - {c}")

                # Ask user for a number
                selection = input("\nEnter the number of the category: ")

                # Validate input
                if not selection.isdigit() or not (1 <= int(selection) <= len(categories)):
                    print("Invalid selection.")
                    continue

                # Convert number to category name
                category = categories[int(selection) - 1]

                # List acronyms in that category
                results = self.manager.list_by_category(category)
                if results:
                    for a in results:
                        print(a)
                else:
                    print("No acronyms found in that category.")

            # Option 3: Add Acronym
            elif choice == "3":
                short = input("Enter acronym: ")
                definition = input("Enter definition: ")
                category = input("Enter category: ")
                self.manager.add_acronym(short, definition, category)
                print("Acronym added successfully.")

            # Option 4: Save to File
            elif choice == "4":
                self.manager.save_to_file()
                print("Acronyms saved to file.")

            # Option 5: Load from File
            elif choice == "5":
                self.manager.load_from_file()
                print("Acronyms loaded from file.")

            # Option 6: Quit
            elif choice == "6":
                print("Goodbye!")
                break

            # Invalid Choice
            else:
                print("Invalid choice. Please try again.")
