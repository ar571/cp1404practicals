"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
It will occur if a non integer value is put in for either the numerator or denominator
2. When will a ZeroDivisionError occur?
It will occur when the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")