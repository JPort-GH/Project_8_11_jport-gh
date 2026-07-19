"""
File: acronym_manager.py
Author: Janet Portillo (Jport-GH)
Date: 2026-06-25
Purpose:
    Manages a collection of Acronym objects. Handles adding, searching,
    listing, saving, and loading acronym data for the VSP Acronym Assistant.
Resources:
    No starter code used. Created for CSCI 1151 Project 1.
"""
from acronym import Acronym
import json

class AcronymManager:
    """
    Manages a list of Acronym objects and provides operations for them.
    """

    def __init__(self):
        """Initialize the manager with an empty acronym list."""
        self.acronyms = []

        # Preloaded VSP Acronyms

        # Strategic Business Units (SBUs) & Roles
        self.add_acronym("SBU", "Strategic Business Unit", "SBUs & Roles")
        self.add_acronym("CMF", "Commercial Markets Field", "SBUs & Roles")
        self.add_acronym("CMM", "Commercial Mid-Market (formerly CMI)", "SBUs & Roles")
        self.add_acronym("SA", "Strategic Alliance", "SBUs & Roles")
        self.add_acronym("GMS", "Government Markets Services", "SBUs & Roles")
        self.add_acronym("D2C", "Direct to Consumer", "SBUs & Roles")
        self.add_acronym("MD", "Market Director (Seller)", "SBUs & Roles")
        self.add_acronym("AM", "Account Manager", "SBUs & Roles")
        self.add_acronym("SAM", "Senior Account Manager", "SBUs & Roles")
        self.add_acronym("SSS", "Sales Support Specialist", "SBUs & Roles")
        self.add_acronym("LSR", "Lead Service Rep", "SBUs & Roles")
        self.add_acronym("LRR", "Lead Renewal Rep", "SBUs & Roles")
        self.add_acronym("RVP", "Regional Vice President", "SBUs & Roles")
        self.add_acronym("SCOS", "Senior Client Operations Specialist", "SBUs & Roles")
        self.add_acronym("MC", "Membership Coordinator", "SBUs & Roles")

        # Systems, Tools & Technology
        self.add_acronym("CASA", "Client Agreement & Structure Administration", "Systems")
        self.add_acronym("SF", "Salesforce", "Systems")
        self.add_acronym("EDI", "Electronic Data Integration/Interface", "Systems")
        self.add_acronym("EM Tool", "Eligibility Management Tool", "Systems")
        self.add_acronym("OC", "Office Central (SharePoint Documents)", "Systems")
        self.add_acronym("E2C", "Email to Case", "Systems")
        self.add_acronym("NRT", "National Reporting Tool", "Systems")
        self.add_acronym("BEI", "Business Enablement & Intelligence", "Systems")

        # Membership & Onboarding Processes
        self.add_acronym("MOB", "Membership Onboarding", "Membership")
        self.add_acronym("CTA", "Converting to Automated", "Membership")
        self.add_acronym("EVR", "Enrollment Verification Report (Tape)", "Membership")
        self.add_acronym("MFC", "Membership File Contact", "Membership")
        self.add_acronym("TPA", "Third Party Administrator", "Membership")
        self.add_acronym("T/M/P", "Term, Merge & Pullout", "Membership")
        self.add_acronym("OE", "Open Enrollment", "Membership")
        self.add_acronym("BOR", "Broker of Record", "Membership")
        self.add_acronym("IRAC", "Issue, Risk, Action, Conclusion", "Membership")

        # Financial, Billing & Underwriting
        self.add_acronym("ASP", "Administrative Service Plan (ASO)", "Financial")
        self.add_acronym("IR", "Individually Rated", "Financial")
        self.add_acronym("PLR", "Paid/Loss Ratio", "Financial")
        self.add_acronym("IBNR", "Incurred But Not Reported", "Financial")
        self.add_acronym("PG", "Performance Guarantee", "Financial")
        self.add_acronym("PEPM", "Per Employee Per Month", "Financial")
        self.add_acronym("PMPM", "Per Member Per Month", "Financial")
        self.add_acronym("LTM", "Last Twelve Months", "Financial")
        self.add_acronym("SIC", "Standard Industrial Classification", "Financial")
        self.add_acronym("FEIN", "Federal Employer Identification Number", "Financial")

        # Plan, Benefit & Network Terms
        self.add_acronym("MBS", "Member Benefit Summary", "Benefits")
        self.add_acronym("EOC", "Evidence of Coverage", "Benefits")
        self.add_acronym("ECL", "Elective Contact Lens", "Benefits")
        self.add_acronym("RFA", "Retail Frame Allowance", "Benefits")
        self.add_acronym("COB", "Coordination of Benefits", "Benefits")
        self.add_acronym("OON", "Out of Network", "Benefits")
        self.add_acronym("GAP", "Group Approved Providers", "Benefits")
        self.add_acronym("AFPR", "Affiliate Provider Retail Chains Partners", "Benefits")
        self.add_acronym("PEC", "Primary Eyecare", "Benefits")
        self.add_acronym("EMEC", "Essential Medical Eye Care", "Benefits")
        self.add_acronym("DEP", "Diabetic Eyecare Program", "Benefits")

    def add_acronym(self, short: str, definition: str, category: str):
        new_acronym = Acronym(short, definition, category)
        self.acronyms.append(new_acronym)

    def search_acronym(self, short: str):
        short = short.lower()
        for acronym in self.acronyms:
            if acronym.short.lower() == short:
                return acronym
        return None

    def list_by_category(self, category: str):
        category = category.lower()
        return [a for a in self.acronyms if a.category.lower() == category]

    def save_to_file(self, filename="acronyms.json"):
        data = []
        for a in self.acronyms:
            data.append({
                "short": a.short,
                "definition": a.definition,
                "category": a.category
            })
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename="acronyms.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            self.acronyms = []
            for item in data:
                self.acronyms.append(
                    Acronym(item["short"], item["definition"], item["category"])
                )
        except FileNotFoundError:
            self.acronyms = []

    def get_categories(self):
        """Return a sorted list of unique categories."""
        categories = {a.category for a in self.acronyms}
        return sorted(categories)
