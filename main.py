#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_letter = random.sample(letters, nr_letters)
random_symbol = random.sample(symbols, nr_symbols)
random_number = random.sample(numbers, nr_numbers)
password = random_letter + random_symbol + random_number
password1 = ''.join(password)
print(f'Your Password is: {password1} "MY CODE" "NOT RAMDOMNIZED"')

#Easy version class example below
pass_word = ''

for  char in range(1, nr_letters + 1):
  pass_word += random.choice(letters)

for  char in range(1, nr_symbols + 1):
  pass_word += random.choice(symbols)

for  char in range(1, nr_numbers + 1):
  pass_word += random.choice(numbers)

print(f'Your Password is: {pass_word} "CLASS CODE" "NOT RAMDOMNIZED"')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_password = random.sample(password, len(password))
password2 = ''.join(random_password)
print(f'Your Password is: {password2} "MY CODE" "RAMDOMNIZED"')

#hard version class example below
pass_word_list = []

for  char in range(1, nr_letters + 1):
  pass_word_list.append(random.choice(letters))

for  char in range(1, nr_symbols + 1):
  pass_word_list.append(random.choice(symbols))

for  char in range(1, nr_numbers + 1):
  pass_word_list.append(random.choice(numbers))

random.shuffle(pass_word_list)
PassWord = ''

for char in pass_word_list:
  PassWord += char
print(f'Your Password is: {PassWord} "CLASS CODE" "RAMDOMNIZED"')
