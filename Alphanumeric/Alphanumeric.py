from datetime import datetime
import re  # To use regular expressions for email validation

class Alpha:
    specificationCount = 0

    @classmethod
    def get_valid_int(cls, prompt, valid_choices=None):
        """Prompt for an integer input and validate it."""
        while True:
            try:
                value = int(input(prompt))
                if valid_choices and value not in valid_choices:
                    print(f"Invalid choice. Please select one of the following: {valid_choices}")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a number.")

    @classmethod
    def get_valid_date(cls, prompt):
        """Prompt for a date input and validate it."""
        while True:
            date_str = input(prompt)
            try:
                return datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    @classmethod
    def get_valid_phone(cls, prompt):
        """Prompt for a valid phone number."""
        while True:
            phone_number = input(prompt)
            if re.match(r"^\+\d{1,15}$", phone_number):
                return phone_number
            else:
                print("Invalid phone number format. Please use the format +1234567890.")

    @classmethod
    def get_valid_email(cls, prompt):
        """Prompt for a valid email address."""
        while True:
            email = input(prompt)
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            else:
                print("Invalid email format. Please enter a valid email address.")

    @classmethod
    def specification(cls):
        ######################################_Password_Specification_#############################################
        print("# Enter Following Password Specifications #")
        passLen = cls.get_valid_int("Enter password length (must be a number): ")
        passSpecial = input("Enter special characters that can be used in the password, separated by commas: ")
        
        ######################################_Target_Specification_################################################
        name = input("Enter target name: ")
        age = cls.get_valid_int("Enter target age: ")
        
        print("Select target gender:")
        print("1. Male")
        print("2. Female")
        gender = cls.get_valid_int("Enter gender (1 or 2): ", valid_choices=[1, 2])
        
        birthdate = cls.get_valid_date("Enter target birthdate (YYYY-MM-DD): ")
        phone_number = cls.get_valid_phone("Enter phone number (e.g., +1234567890): ")
        email_address = cls.get_valid_email("Enter email address: ")

        print("Select target marital status:")
        print("1. Married")
        print("2. Unmarried")
        marital_status = cls.get_valid_int("Enter marital status (1 or 2): ", valid_choices=[1, 2])
        
        num_children = 0  # Initialize to zero or None, assuming this may not apply
        if marital_status == 1:
            num_children = cls.get_valid_int("Enter number of children: ")

        # Save or process the data here, e.g., write to a file or database
        cls.save_specification({
            'name': name,
            'age': age,
            'gender': gender,
            'birthdate': birthdate.strftime("%Y-%m-%d"),
            'phone_number': phone_number,
            'email_address': email_address,
            'marital_status': marital_status,
            'num_children': num_children,
            'passLen': passLen,
            'passSpecial': passSpecial
        })
        
        print("Specifications have been recorded.")

    @classmethod
    def save_specification(cls, data):
        """
        Saves the specification data to a file.
        This could be expanded to save to a database or other storage.
        """
        with open("specifications.txt", "a") as f:
            f.write(str(data) + "\n")
        print("Specifications saved successfully.")

# Example usage
if __name__ == "__main__":
    Alpha.specification()
