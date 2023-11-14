import random
import string

def generate_password(length=12):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure at least one character from each set
    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(digits) + random.choice(special_characters)

    # Generate the rest of the password
    for _ in range(length - 4):
        password += random.choice(all_characters)

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Example: Generate a strong password with a length of 16 characters
password = generate_password(16)
print(password)
