import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
separator = ""

print("Welcome to the Random Password Generator")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

letter_elements = random.sample(letters, num_letters)
random_letters = separator.join(letter_elements)

symbols_elements = random.sample(symbols, num_symbols)
random_symbols = separator.join(symbols_elements)

number_elements = random.sample(numbers, num_numbers)
random_numbers = separator.join(number_elements)

p = random_letters + random_symbols + random_numbers
password_list = list(p)

random.shuffle(password_list)
random_password = ''.join(password_list)

print(random_password)