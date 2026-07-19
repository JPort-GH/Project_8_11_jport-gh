"""
File: acronym.py
Author: Janet Portillo (Jport-GH)
Date: 2026-06-25
Purpose:
    Defines the Acronym class used in the VSP Acronym Assistant project.
    Includes a subclass (SystemAcronym) to demonstrate inheritance as required
    in Chapters 8–11. Represents acronym entries with their definition and category.
Resources:
    No starter code used. Created for CSCI 1151 Project 8–11.
"""

class Acronym:
    """
    Represents a single acronym entry with its definition and category.
    Base class for all acronym types.
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


class SystemAcronym(Acronym):
    """
    Represents acronyms specifically used for systems/tools.
    Demonstrates inheritance from the Acronym base class.
    """

    def __init__(self, short: str, definition: str):
        """
        Initialize a SystemAcronym object.

        Parameters:
            short (str): Acronym text (e.g., 'EDI').
            definition (str): Full meaning of the acronym.

        Category is automatically set to 'Systems'.
        """
        super().__init__(short, definition, "Systems")
