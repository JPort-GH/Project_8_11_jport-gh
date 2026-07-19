"""
File: acronym_manager.py
Author: Janet Portillo (Jport-GH)
Date: 2026-06-25
Purpose:
    Manages a collection of Acronym objects. Handles adding, searching,
    listing, saving, and loading acronym data for the VSP Acronym Assistant.
    Uses external JSON files to reduce nesting and improve modularity.
Resources:
    No starter code used. Created for CSCI 1151 Project 8–11.
"""

import json
import os
from acronym import Acronym


class AcronymManager:
    """
    Manages a list of Acronym objects and provides operations for them.
    Loads predefined acronyms from an external JSON file to avoid deep nesting.
    """

    def __init__(self, preload_file="preloaded_acronyms.json"):
        """
        Initialize the manager with an empty acronym list.
        Load predefined acronyms from a JSON file if available.
        """
        self.acronyms = []

        if os.path.exists(preload_file):
            self._load_predefined(preload_file)
        else:
            print(f"Warning: Preload file '{preload_file}' not found. No acronyms loaded.")

    # ------------------------------------------------------------
    # Load predefined acronyms (Chapter 9–11: JSON + modularization)
    # ------------------------------------------------------------

    def _load_predefined(self, filename):
        """
        Load predefined acronyms from a JSON file.

        Expected JSON structure:
        {
            "file": "...",
            "author": "...",
            "date": "...",
            "purpose": "...",
            "source": "...",
            "acronyms": [
                {"short": "...", "definition": "...", "category": "..."},
                ...
            ]
        }
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            acronym_items = data.get("acronyms", [])

            for item in acronym_items:
                self.add_acronym(item["short"], item["definition"], item["category"])

        except json.JSONDecodeError:
            print(f"Error: '{filename}' contains invalid JSON.")
        except Exception as e:
            print(f"Unexpected error loading predefined acronyms: {e}")

    # ------------------------------------------------------------
    # Core functionality
    # ------------------------------------------------------------

    def add_acronym(self, short: str, definition: str, category: str):
        """
        Add a new acronym to the internal list.

        Parameters:
            short (str): Acronym text (e.g., 'EDI').
            definition (str): Full meaning of the acronym.
            category (str): Category the acronym belongs to.
        """
        new_acronym = Acronym(short, definition, category)
        self.acronyms.append(new_acronym)

    def search_acronym(self, short: str):
        """
        Search for an acronym by its short code.

        Parameters:
            short (str): Acronym text to search for.

        Returns:
            Acronym or None: Matching Acronym object if found.
        """
        short = short.lower()
        for acronym in self.acronyms:
            if acronym.short.lower() == short:
                return acronym
        return None

    def list_by_category(self, category: str):
        """
        Retrieve all acronyms belonging to a specific category.

        Parameters:
            category (str): Category name to filter by.

        Returns:
            list[Acronym]: Acronyms in the given category.
        """
        category = category.lower()
        return [a for a in self.acronyms if a.category.lower() == category]

    def save_to_file(self, filename="acronyms.json"):
        """
        Save all acronym data to a JSON file.

        Parameters:
            filename (str): File path to save acronym data.
        """
        data = [
            {
                "short": a.short,
                "definition": a.definition,
                "category": a.category
            }
            for a in self.acronyms
        ]

        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving acronyms: {e}")

    def load_from_file(self, filename="acronyms.json"):
        """
        Load acronym data from a JSON file and merge with existing data.

        Behavior:
            - Only new acronyms (based on short code) are added.
            - Existing acronyms are not overwritten.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            existing_shorts = {a.short for a in self.acronyms}

            for item in data:
                if item["short"] not in existing_shorts:
                    self.add_acronym(item["short"], item["definition"], item["category"])

        except FileNotFoundError:
            print("No saved file found. Nothing loaded.")
        except json.JSONDecodeError:
            print(f"Error: '{filename}' contains invalid JSON.")
        except Exception as e:
            print(f"Unexpected error loading acronyms: {e}")

    def get_categories(self):
        """
        Return a sorted list of unique acronym categories.

        Returns:
            list[str]: Alphabetically sorted category names.
        """
        categories = {a.category for a in self.acronyms}
        return sorted(categories)
