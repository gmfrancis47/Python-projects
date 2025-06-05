import random
import string

def generate_password(length=12, use_special=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters + digits
    if use_special:
        characters += specials

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for settings
try:
    length = int(input("Enter password length (e.g., 12): "))
except ValueError:
    length = 12

use_special = input("Include special characters? (y/n): ").lower() == 'y'

password = generate_password(length, use_special)
print(f"\n🔐 Your new password: {password}")
