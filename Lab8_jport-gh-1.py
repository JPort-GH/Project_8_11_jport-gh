"""
Program Name: Lab8_jport-gh-1.py
Author: Janet Portillo
Purpose: Validate a 12-digit UPC-A code by calculating the correct check digit
         and comparing it to the user-provided check digit.
Starter Code: No external starter code used.
Date: 06/21/2026
"""

def find_UPC(first11):
    
    #Calculates and returns the correct UPC-A check digit based on the first 11 digits.

    odd_sum = 0
    for i in range(0, 11, 2):
        odd_sum += int(first11[i])

    odd_sum *= 3

    even_sum = 0
    for i in range(1, 11, 2):
        even_sum += int(first11[i])

    total = odd_sum + even_sum

    check_digit = (10 - (total % 10)) % 10
    return check_digit

# MAIN PROGRAM
while True:
    upc = input("Enter a 12-digit UPC: ")

    # Optional challenge: input validation
    if len(upc) != 12 or not upc.isdigit():
        print("Error: UPC must be exactly 12 digits and contain only numbers.\n")
        continue

    break  # valid input

first11 = upc[:11]
provided_check = upc[11]

print(f"\nThe first 11 digits are '{first11}'.")
print(f"The provided check digit is '{provided_check}'.\n")

print("Calculating...")
expected_check = find_UPC(first11)

print(f"The expected check digit is {expected_check}.\n")

if str(expected_check) == provided_check:
    print("This is a VALID UPC.")
else:
    print("This is an INVALID UPC.")
