import random
import string

def generate_password():
    # Define character sets for each category
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    special_characters = string.punctuation
    numbers = string.digits

    # Generate one character from each category
    password = random.choice(uppercase_letters)
    password += random.choice(lowercase_letters)
    password += random.choice(special_characters)
    password += random.choice(numbers)

    # Shuffle the characters to randomize the password
    password = ''.join(random.sample(password, len(password)))

    return password

# Generate and print the password
password = generate_password()
print("Generated Password:", password)
