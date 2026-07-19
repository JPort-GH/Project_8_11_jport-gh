"""
File: main.py
Author: Janet Portillo (Jport-GH)
Date: 2026-06-25
Purpose:
    Entry point for the VSP Acronym Assistant. Runs the application.
Resources:
    No starter code used. Created for CSCI 1151 Project 1.
"""
from app import AcronymApp

def main():
    """
    Run the VSP Acronym Assistant application.
    """
    app = AcronymApp()
    app.run()

if __name__ == "__main__":
    main()