import os
import random
import string
import datetime

# Load the list of words from the provided file
def load_words(filepath):
    with open(filepath, 'r') as file:
        words = file.read().splitlines()
    return words

# Generate a memorable password
def generate_memorable_password(num_words, case_option, word_list):
    password = []
    for _ in range(num_words):
        word = random.choice(word_list)
        if case_option == 'lower':
            word = word.lower()
        elif case_option == 'upper':
            word = word.upper()
        elif case_option == 'capitalize':
            word = word.capitalize()
        random_digit = str(random.randint(0, 9))
        password.append(f"{word}{random_digit}")
    return '-'.join(password)

# Generate a random password
def generate_random_password(length, include_punctuation, exclude_chars=None):
    characters = string.ascii_letters + string.digits
    if include_punctuation:
        characters += string.punctuation
    if exclude_chars:
        characters = ''.join([ch for ch in characters if ch not in exclude_chars])

    return ''.join(random.choice(characters) for _ in range(length))

# Log/w timestamp
def log_password(directory, password):
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, "Generated_Passwords.txt")
    timestamp = datetime.datetime.now().strftime('%A, %B %d, %Y %H:%M:%S')
    with open(filepath, 'a') as file:
        file.write(f"{password} - Created on {timestamp}\n")

# Main generator function 
def password_generator():
    word_list = load_words("top_english_nouns_lower_100000.txt")
    
    for _ in range(1000):  
        password_type = random.choice(['memorable', 'random'])

        if password_type == 'memorable':
            num_words = random.randint(3, 5)  # Example: Choose between 3 to 5 words
            case_option = random.choice(['lower', 'upper', 'capitalize'])
            password = generate_memorable_password(num_words, case_option, word_list)
            log_password("Memorable", password)

        elif password_type == 'random':
            length = random.randint(8, 16)  # Example: Choose specified password length 
            include_punctuation = random.choice([True, False])
            exclude_chars = random.choice([None, "l1O0"])  
            password = generate_random_password(length, include_punctuation, exclude_chars)
            log_password("Random", password)

# Run the password generator
password_generator()
