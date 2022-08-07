"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

OUTPUT_FILE = "./price.txt"
INITIAL_PRICE = 10
MIN_PRICE = 0.01
MAX_PRICE = 1000
MIN_INCREASE = 0
MAX_INCREASE = 10
MIN_DECREASE = 0
MAX_DECREASE = 5

def main():
    days = 0
    price = INITIAL_PRICE
    out_file = open(OUTPUT_FILE, 'w')

    print(f"Starting price: ${price:.2f}", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        if random.randint(0, 1) == 0:
            increase = random.randint(MIN_INCREASE, MAX_INCREASE)
            price = price + (price * increase / 100)
        else:
            decrease = random.randint(MIN_DECREASE, MAX_DECREASE)
            price = price - (price * decrease / 100)
        days += 1
        print(f"On day {days} price is: ${price:.2f}", file=out_file)

    out_file.close()


main()