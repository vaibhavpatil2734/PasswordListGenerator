from datetime import datetime
import re  # To use regular expressions for email validation
import uuid  # To generate unique identifiers

class Alpha:
    specificationCount = 0

    @classmethod
    def get_valid_int(cls, prompt, valid_choices=None):
        """Prompt for an integer input and validate it."""
        while True:
            value = input(prompt)
            if value.lower() in ["exit", '-']:
                return None  # Treat '-' and 'exit' as None
            try:
                value = int(value)
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
            if date_str.lower() in ["exit", '-']:
                return None  # Treat '-' and 'exit' as None
            try:
                return datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    @classmethod
    def get_valid_phone(cls, prompt):
        """Prompt for a valid phone number."""
        while True:
            phone_number = input(prompt)
            if phone_number.lower() in ["exit", '-']:
                return None  # Treat '-' and 'exit' as None
            if re.match(r"^\+\d{1,15}$", phone_number):
                return phone_number
            else:
                print("Invalid phone number format. Please use the format +1234567890.")

    @classmethod
    def get_valid_email(cls, prompt):
        """Prompt for a valid email address."""
        while True:
            email = input(prompt)
            if email.lower() in ["exit", '-']:
                return None  # Treat '-' and 'exit' as None
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            else:
                print("Invalid email format. Please enter a valid email address.")

    @classmethod
    def get_multiple_inputs(cls, prompt):
        """Prompt for multiple inputs until 'exit' or '-' is entered."""
        items = []
        sr_No = 1
        while True:
            item = input(f"{prompt} #{sr_No}: ")
            if item.lower() in ["exit", '-']:
                break
            items.append(item)
            sr_No += 1
        return items


#################################################################################################################
######################################_Password_Specification_################################################
#################################################################################################################

    @classmethod
    def password_Specification(cls):
        print("# Enter Following Password Specifications #")
        passLen = cls.get_valid_int("Enter password length (must be a number): ")
        passSpecial = input("Enter special characters that can be used in the password, separated by commas: ")


#################################################################################################################
######################################_Target_Specification_################################################
#################################################################################################################

    @classmethod
    def target_Specification(cls):
        print("## Enter Following Target Specifications ##")
        print("You can skip any field by entering '-' or type 'exit' to stop.")

        ### Level 1 ###
        level_1 = {
            'name': input("Enter target name (or '-' to skip): ") or None,
            'nicknames': cls.get_multiple_inputs("Enter nickname (or '-' to skip)")
        }

        ### Level 2 ###
        birthdate = cls.get_valid_date("Enter target birthdate (YYYY-MM-DD) or '-' to skip: ")
        level_2 = {
            'birthdate': birthdate.strftime("%Y-%m-%d") if birthdate else None,
            'special_dates': cls.get_multiple_inputs("Enter special date (e.g., marriage or achievement date) (or '-' to skip)"),
            'phone_numbers': cls.get_multiple_inputs("Enter phone number (e.g., +1234567890) (or '-' to skip)"),
            'vehicle_numbers': cls.get_multiple_inputs("Enter vehicle number (or '-' to skip)"),
            'house_number': input("Enter house number (or '-' to skip): ") or None,
            'special_identity_numbers': cls.get_multiple_inputs("Enter special identity number (e.g., roll number, emp number) (or '-' to skip)")
        }

        ### Level 3 ###
        level_3 = {
            'email_addresses': cls.get_multiple_inputs("Enter email address (or '-' to skip)"),
            'social_media_usernames': cls.get_multiple_inputs("Enter social media account username (or '-' to skip)"),
            'game_ids': cls.get_multiple_inputs("Enter game ID (or '-' to skip)")
        }

        ### Level 4 ###
        level_4 = {
            'work_areas': cls.get_multiple_inputs("Enter work area (e.g., company name, school name, college name) (or '-' to skip)"),
            'favorite_movies': cls.get_multiple_inputs("Enter favorite movie (or '-' to skip)"),
            'favorite_sports': cls.get_multiple_inputs("Enter favorite sport (or '-' to skip)"),
            'favorite_superstars': input("Enter favorite superstar or celebrity (or '-' to skip): ") or None,
            'favorite_video_games': cls.get_multiple_inputs("Enter favorite video game (or '-' to skip)"),
            'favorite_singers': cls.get_multiple_inputs("Enter favorite singer (or '-' to skip)"),
            'hobbies': cls.get_multiple_inputs("Enter hobbies (or '-' to skip)"),
            'achievements': cls.get_multiple_inputs("Enter achievements (or '-' to skip)")
        }

        # Save the dictionaries
        cls.save_specification("target_specifications.txt", {
            'Level 1': level_1,
            'Level 2': level_2,
            'Level 3': level_3,
            'Level 4': level_4
        })

        print("Target specifications have been recorded.")


#################################################################################################################
######################################_Suspect_Specification_################################################
#################################################################################################################

    @classmethod
    def suspect_Specification(cls):

        print("## Enter Following Suspect Specifications ##")
        print("You can skip any field by entering '-' or type 'exit' to stop.")

        suspect_id = str(uuid.uuid4())  # Generate a unique identifier for each suspect

        ### Level 1 ###
        level_1 = {
            'name': input("Enter suspect name (or '-' to skip): ") or None,
            'nicknames': cls.get_multiple_inputs("Enter nickname (or '-' to skip)")
        }

        ### Level 2 ###
        level_2 = {
            'birth_date':cls.input(),
            'special_dates': cls.get_multiple_inputs("Enter special date (e.g., marriage or achievement date) (or '-' to skip)"),
            'phone_numbers': cls.get_multiple_inputs("Enter phone number (e.g., +1234567890) (or '-' to skip)"),
            'vehicle_numbers': cls.get_multiple_inputs("Enter vehicle number (or '-' to skip)"),
            'house_number': input("Enter house number (or '-' to skip): ") or None,
            'special_identity_numbers': cls.get_multiple_inputs("Enter special identity number (e.g., roll number, emp number) (or '-' to skip)")
        }

        ### Level 3 ###
        level_3 = {
            'email_addresses': cls.get_multiple_inputs("Enter email address (or '-' to skip)"),
            'game_ids': cls.get_multiple_inputs("Enter game ID (or '-' to skip)")
        }

        ### Level 4 ###
        level_4 = {
            'favorite_movies': cls.get_multiple_inputs("Enter favorite movie (or '-' to skip)"),
            'favorite_sports': cls.get_multiple_inputs("Enter favorite sport (or '-' to skip)"),
            'favorite_superstars': input("Enter favorite superstar or celebrity (or '-' to skip): ") or None,
            'favorite_video_games': cls.get_multiple_inputs("Enter favorite video game (or '-' to skip)"),
            'social_media_usernames': cls.get_multiple_inputs("Enter social media account username (or '-' to skip)"),
            'favorite_singers': cls.get_multiple_inputs("Enter favorite singer (or '-' to skip)"),
            'hobbies': cls.get_multiple_inputs("Enter hobbies (or '-' to skip)"),
            'achievements': cls.get_multiple_inputs("Enter achievements (or '-' to skip)"),
            'work_areas': cls.get_multiple_inputs("Enter work area (e.g., company name, school name, college name) (or '-' to skip)")
        }

        # Save the dictionaries
        cls.save_specification("suspect_specifications.txt", {
            'suspect_id': suspect_id,
            'Level 1': level_1,
            'Level 2': level_2,
            'Level 3': level_3,
            'Level 4': level_4
        })

        print("Suspect specifications have been recorded.")

    @classmethod
    def save_specification(cls, filename, data):
        """Save the specification data to a file."""
        with open(filename, "a") as f:
            f.write(str(data) + "\n")
        print(f"Specifications saved successfully to {filename}.")



#################################################################################################################
#################################################### DS & Generator #############################################################
#################################################################################################################

    @classmethod
    def generator_Atom(cls):
        """Extract and store level-wise values from the file into arrays."""
        level_1_values = []
        level_2_values = []
        level_3_values = []
        level_4_values = []

        with open("target_specifications.txt", "r") as file:
            data = eval(file.read())  # Reading the dictionary data from the file

        for key, level_data in data.items():
            if key == "Level 1":
                for value in level_data.values():
                    if isinstance(value, list):
                        level_1_values.extend(value)
                    elif value:
                        level_1_values.append(value)

            elif key == "Level 2":
                for value in level_data.values():
                    if isinstance(value, list):
                        level_2_values.extend(value)
                    elif value:
                        level_2_values.append(value)

            elif key == "Level 3":
                for value in level_data.values():
                    if isinstance(value, list):
                        level_3_values.extend(value)
                    elif value:
                        level_3_values.append(value)

            elif key == "Level 4":
                for value in level_data.values():
                    if isinstance(value, list):
                        level_4_values.extend(value)
                    elif value:
                        level_4_values.append(value)

######################################_Templates_################################################
        level_2_PD =[]
        
        cleandata=[]
        for i in level_2_values:
            value = re.sub('-','',i)
            cleandata.append(value)

        for i in cleandata:
            for length in range(1, len(i) + 1):  # Length from 1 to length of i
                for start in range(len(i) - length + 1):  # Starting index for the substring
                    substring = i[start:start + length]  # Get the substring of the specified length
                    level_2_PD.append(substring)
            break

            
        print(level_2_PD)
        
  





if __name__ == "__main__":
    
    # Alpha.target_Specification()
   # Alpha.suspect_Specification()
    Alpha.generator_Atom()
  

    # input_One = input("If you want to add target specifications, enter 'y': ")
    # input_Two = input("If you want to add suspect specifications, type 'suspect', otherwise type 'exit': ")
    # if input_Two.lower() == 'suspect':
    #     Alpha.suspect_Specification()
