from datetime import datetime

class Alpha:
    specificationCount = 0

    @classmethod
    def specification(cls):
        # Prompt user for input
        try:
            passLen = int(input("Enter password length: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        name = input("Enter target name: ")

        try:
            age = int(input("Enter target age: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        print("Select target gender:")
        print("1. Male")
        print("2. Female")
        try:
            gender = int(input("Enter gender (1 or 2): "))
            if gender not in [1, 2]:
                print("Invalid input. Please select 1 for Male or 2 for Female.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        print("Select target marital status:")
        print("1. Married")
        print("2. Unmarried")
        try:
            marital_status = int(input("Enter marital status (1 or 2): "))
            if marital_status not in [1, 2]:
                print("Invalid input. Please select 1 for Married or 2 for Unmarried.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        birthdate = input("Enter target birthdate (YYYY-MM-DD): ")
        try:
            birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        try:
            num_children = int(input("Enter number of children: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        phone_number = input("Enter phone number (e.g., +1234567890): ")
        email_address = input("Enter email address: ")

        # Output collected information for confirmation
        print("\nCollected Information:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Gender: {'Male' if gender == 1 else 'Female'}")
        print(f"Marital Status: {'Married' if marital_status == 1 else 'Unmarried'}")
        print(f"Birthdate: {birthdate.strftime('%Y-%m-%d')}")
        print(f"Number of Children: {num_children}")
        print(f"Phone Number: {phone_number}")
        print(f"Email Address: {email_address}")

        # You can now use this information to generate passwords or for other purposes

# Example usage
if __name__ == "__main__":
    Alpha.specification()
