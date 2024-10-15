import random
import string

# Sample data for generating passwords
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
birth_years = ["1985", "1990", "1995", "2000", "2005"]
favorite_numbers = ["7", "42", "13", "99", "21"]
special_chars = ["!", "@", "#", "$", "%", "&", "*"]

# Password templates (distinct)
templates = [
    "{name}{birth_year}",                  # Example: Alice1985
    "{name}{special_char}{favorite_number}", # Example: Bob!42
    "{favorite_number}{name}{birth_year}",   # Example: 7Charlie1995
    "{birth_year}{favorite_number}{special_char}", # Example: 200521$
    "{name}{birth_year}{special_char}",     # Example: David1990#
    "{favorite_number}{special_char}{name}", # Example: 99*Eve
    "{name}@{favorite_number}",              # Example: Charlie@13
    "{birth_year}_{name}",                   # Example: 1995_Bob
    "{name}{special_char}{name}",            # Example: Alice!Alice
    "{favorite_number}{birth_year}",         # Example: 42_2000
]

def generate_passwords(num_passwords):
    password_list = []
    for _ in range(num_passwords):
        # Choose a random template
        template = random.choice(templates)

        # Fill the template with random data
        password = template.format(
            name=random.choice(names),
            birth_year=random.choice(birth_years),
            favorite_number=random.choice(favorite_numbers),
            special_char=random.choice(special_chars)
        )
        password_list.append(password)

    return password_list

def main():
    num_passwords = 10  # Number of passwords to generate
    passwords = generate_passwords(num_passwords)

    # Print the generated passwords
    print("Generated Passwords:")
    for idx, pwd in enumerate(passwords):
        print(f"{idx + 1}: {pwd}")

if __name__ == "__main__":
    main()
