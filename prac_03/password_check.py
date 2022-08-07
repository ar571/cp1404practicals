MIN_LENGTH = 10

def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print("Password is too short")
        password = input("Enter your password: ")
    return password


main()