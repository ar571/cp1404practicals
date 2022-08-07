import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# line 1: i saw 16, smallest possible number would be 5 and largest 20
# line 2: i saw 9, smallest possible number would be 3, largest would be 9. no it cannot produce a 4
# line 3: i saw 3.225 (shortened to 3 decimal points), smallest would be 2.5, largest 5.5

print(random.randint(1, 100))