import string
import random
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
number_letter = int(input("How many letters? "))
number_digit = int(input("How many digits? "))
number_special = int(input("How many special chars?" ))
character_pool = []
character_pool.extend(random.choices(letters, k=number_letter))
character_pool.extend(random.choices(digits, k=number_digit))
character_pool.extend(random.choices(special_chars, k=number_special))
random.shuffle(character_pool)
final_password = ''.join(character_pool)
print("Generated Password:", final_password)