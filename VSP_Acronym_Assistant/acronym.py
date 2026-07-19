"""
File: acronym.py
Author: Janet Portillo (Jport-GH)
Date: 2026-06-25
Purpose:
    Defines the Acronym class used in the VSP Acronym Assistant project.
    This class represents a single acronym, its definition, and its category.
Resources:
    No starter code used. Created for CSCI 1151 Project 1.
"""
class Acronym:
    """
    Represents a single acronym entry with its definition and category.
    """

    def __init__(self, short: str, definition: str, category: str):
        """
        Initialize an Acronym object.

        Parameters:
            short (str): The acronym text (e.g., 'EDI').
            definition (str): The full meaning of the acronym.
            category (str): The category this acronym belongs to.
        """
        self.short = short
        self.definition = definition
        self.category = category

    def __str__(self):
        """
        Return a readable string representation of the acronym.
        """
        return f"{self.short}: {self.definition} ({self.category})" 