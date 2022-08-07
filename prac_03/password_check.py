MIN_LENGTH = 10

password = input("Enter your password: ")
while len(password) < MIN_LENGTH:
    print("Password is too short")
    password = input("Enter your password: ")

print("*" * len(password))