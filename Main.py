import itertools
import random
import string

def get_user_input():
    """ Get input from the user for password generation. """
    name = input("Enter target name (or leave blank): ").strip()
    birthdate = input("Enter target birthdate (DDMMYYYY or leave blank): ").strip()
    surname = input("Enter target surname (or leave blank): ").strip()
    company = input("Enter company name (or leave blank): ").strip()
    platform = input("Enter platform name (or leave blank): ").strip()
    nickname = input("Enter nickname (or leave blank): ").strip()
    favorite_color = input("Enter favorite color (or leave blank): ").strip()
    favorite_sport = input("Enter favorite sport (or leave blank): ").strip()
    pet_name = input("Enter pet's name (or leave blank): ").strip()
    lucky_number = input("Enter lucky number (or leave blank): ").strip()
    keywords = input("Enter important keywords separated by commas (or leave blank): ").strip().split(',')
    family_details = input("Enter family details (e.g., names, birthdates) separated by commas (or leave blank): ").strip().split(',')

    keywords = [kw.strip() for kw in keywords if kw.strip()]
    family_details = [fd.strip() for fd in family_details if fd.strip()]

    return name, birthdate, surname, company, platform, nickname, favorite_color, favorite_sport, pet_name, lucky_number, keywords, family_details

def generate_passwords(name, birthdate, surname, company, platform, nickname, favorite_color, favorite_sport, pet_name, lucky_number, keywords, family_details):
    """ Generate passwords based on user input. """
    passwords = set()

    # Function to create password variations
    def create_variations(parts):
        for length in range(1, 9):  # Maximum length of 8
            for combination in itertools.permutations(parts, length):
                password = ''.join(combination)
                if len(password) <= 8:
                    yield password

    # Create parts from user inputs
    parts = [name, surname, company, platform, nickname, favorite_color, favorite_sport, pet_name, lucky_number] + keywords + family_details
    parts = [part for part in parts if part]  # Remove empty strings

    # Add variations with birthdate and special characters
    if birthdate:
        parts.append(birthdate[:4])  # Year
        parts.append(birthdate[2:4])  # Month
        parts.append(birthdate[:2])  # Day
    special_chars = '!@#$%^&*'

    # Generate password variations
    for password in create_variations(parts):
        # Ensure password has uppercase, lowercase, digit, and special character
        if any(c.islower() for c in password):
            password = password.capitalize()  # Ensure at least one uppercase
        if not any(c.isdigit() for c in password):
            password += random.choice(string.digits)
        if not any(c in special_chars for c in password):
            password += random.choice(special_chars)

        if len(password) <= 8:
            passwords.add(password)
        
        if len(passwords) >= 1000:
            break

    return list(passwords)

def main():
    """ Main function to run the script. """
    user_input = get_user_input()
    passwords = generate_passwords(*user_input)
    
    # Ensure at least 50 passwords are generated
    if len(passwords) < 50:
        print("Generated less than 50 passwords. Please provide more input data or adjust the input.")
    else:
        # Save passwords to a file
        with open("passwords.txt", "w") as file:
            for password in passwords:
                file.write(password + "\n")
        
        print(f"Generated {len(passwords)} passwords and saved to passwords.txt")

if __name__ == "__main__":
    main()
