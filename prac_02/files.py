name_file = open('./name.txt', 'w')
name = input("Enter your name: ")
print(name, file=name_file)
name_file.close()

name_file = open('./name.txt', 'r')
print(f"Your name is {name_file.read()}")
name_file.close()

number_file = open('./numbers.txt', 'r')
num1 = int(number_file.readline())
num2 = int(number_file.readline())
result = num1 + num2
print(result)
number_file.close()

number_file = open('./numbers.txt', 'r')
result = 0
for line in number_file:
    value = int(line)
    result += value
print(result)
number_file.close()