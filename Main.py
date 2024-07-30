def generate_passwords(name, birthdate, surname, company, platform, keywords):
    """ Generate passwords based on user input. """
    passwords = set()

    # Function to create password variations
    def create_variations(parts):
        for length in range(8, 12):
            for combination in itertools.permutations(parts, min(length, len(parts))):
                for perm in itertools.permutations(combination, length):
                    yield ''.join(perm)

    # Create parts from user inputs
    parts = [name, birthdate, surname, company, platform]
    parts = [part for part in parts if part]  # Remove empty strings
    if keywords:
        parts.extend(keywords)

    print(f"Parts: {parts}")

    # Generate password variations
    for password in create_variations(parts):
        # Ensure password is valid
        if (len(password) >= 8 and 
            any(c.isupper() for c in password) and 
            any(c.islower() for c in password) and 
            any(c.isdigit() for c in password) and 
            any(c in string.punctuation for c in password)):
            passwords.add(password)
        
        if len(passwords) >= 10000:
            break

    print(f"Generated passwords: {passwords}")
    return list(passwords)

def main():
    """ Main function to run the script. """
    name, birthdate, surname, company, platform, keywords = get_user_input()
    passwords = generate_passwords(name, birthdate, surname, company, platform, keywords)
    
    # Save passwords to a file
    with open("passwords.txt", "w") as file:
        for password in passwords:
            file.write(password + "\n")
    
    print(f"Generated {len(passwords)} passwords and saved to passwords.txt")

if __name__ == "__main__":
    main()
