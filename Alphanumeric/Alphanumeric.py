from datetime import datetime

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
    def specification(cls):
        ######################################_Password_Specification_#############################################
        print("# Enter Following Password Specifications #")
        passLen = cls.get_valid_int("Enter password length: ")
        passSpecial  = input("Enter Special Characters that we can use in pasword seperated by commas: ")
        ######################################_Target_Specification_################################################
        name = input("Enter target name: ")
        age = cls.get_valid_int("Enter target age: ")
        gender = cls.get_valid_int("Enter gender (1 or 2): ", valid_choices=[1, 2])
        birthdate = cls.get_valid_date("Enter target birthdate (YYYY-MM-DD): ")
        phone_number = input("Enter phone number (e.g., +1234567890): ")
        email_address = input("Enter email address: ")

        print("Select target gender:")
        print("1. Male")
        print("2. Female")

        print("Select target marital status:")
        print("1. Married")
        print("2. Unmarried")
        marital_status = cls.get_valid_int("Enter marital status (1 or 2): ", valid_choices=[1, 2])
        if(marital_status == 1):
                    num_children = cls.get_valid_int("Enter number of children: ")




#its time to start the actual coding

# Example usage
if __name__ == "__main__":
    Alpha.specification()
