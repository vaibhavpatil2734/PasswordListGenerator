from datetime import datetime
import re  # To use regular expressions for email validation
import uuid  # To generate unique identifiers
import json

class Alpha:
    specificationCount = 0

    @classmethod
    def get_valid_int(cls, prompt, valid_choices=None):
        """Prompt for an integer input and validate it."""
        while True:
            value = input(prompt)
            if value == "":  # Skip the field if the user presses "Enter"
                return None
            try:
                value = int(value)
                if valid_choices and value not in valid_choices:
                    print(f"Invalid choice. Please select one of the following: {valid_choices}")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a number.")

    @classmethod
    def get_valid_date_parts(cls):
        """Prompt for year, month, and day separately, and validate the date."""
        while True:
            try:
                year = input("Enter birth year (YYYY) or press Enter to skip: ")
                if year == "":  # Skip if no input
                    return None

                year = int(year)
                
                month = input("Enter birth month (MM) or press Enter to skip: ")
                if month == "":
                    return None
                month = int(month)

                day = input("Enter birth day (DD) or press Enter to skip: ")
                if day == "":
                    return None
                day = int(day)

                return datetime(year, month, day)  # Combine the parts into a datetime object

            except ValueError:
                print("Invalid date. Please enter a valid birth year, month, and day.")

    @classmethod
    def get_name_parts(cls):
        """Prompt for first, middle, and last name."""
        first_name = input("Enter first name (or press Enter to skip): ") or None
        middle_name = input("Enter middle name (or press Enter to skip): ") or None
        last_name = input("Enter last name (or press Enter to skip): ") or None

        return {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name
        }

    @classmethod
    def get_multiple_inputs(cls, prompt):
        """Prompt for multiple inputs until 'Enter' is pressed without input."""
        items = []
        sr_No = 1
        while True:
            item = input(f"{prompt} #{sr_No} (or press Enter to skip): ")
            if item == "":  # Stop if user presses "Enter" without input
                break
            items.append(item)
            sr_No += 1
        return items


#################################################################################################################
######################################_Target_Specification_################################################
#################################################################################################################

    @classmethod
    def target_Specification(cls):
        print("## Enter Following Target Specifications ##")
        print("You can skip any field by pressing 'Enter'.")

        ### Level 1 ###
        level_1 = {
            'name': cls.get_name_parts(),
            'nicknames': cls.get_multiple_inputs("Enter nickname")
        }

        ### Level 2 ###
        birthdate = cls.get_valid_date_parts()  # Take year, month, day separately
        level_2 = {
            'birthdate': birthdate.strftime("%Y-%m-%d") if birthdate else None,
            'special_dates': cls.get_multiple_inputs("Enter special date (e.g., marriage or achievement date)"),
            'phone_numbers': cls.get_multiple_inputs("Enter phone number (e.g., +1234567890)"),
            'vehicle_numbers': cls.get_multiple_inputs("Enter vehicle number"),
            'house_number': input("Enter house number (or press Enter to skip): ") or None,
            'special_identity_numbers': cls.get_multiple_inputs("Enter special identity number (e.g., roll number, emp number)")
        }

        ### Level 3 ###
        level_3 = {
            'email_addresses': cls.get_multiple_inputs("Enter email address"),
            'social_media_usernames': cls.get_multiple_inputs("Enter social media account username"),
            'game_ids': cls.get_multiple_inputs("Enter game ID")
        }

        ### Level 4 ###
        level_4 = {
            'work_areas': cls.get_multiple_inputs("Enter work area (e.g., company name, school name, college name)"),
            'favorite_movies': cls.get_multiple_inputs("Enter favorite movie"),
            'favorite_sports': cls.get_multiple_inputs("Enter favorite sport"),
            'favorite_superstars': input("Enter favorite superstar or celebrity (or press Enter to skip): ") or None,
            'favorite_video_games': cls.get_multiple_inputs("Enter favorite video game"),
            'favorite_singers': cls.get_multiple_inputs("Enter favorite singer"),
            'hobbies': cls.get_multiple_inputs("Enter hobbies"),
            'achievements': cls.get_multiple_inputs("Enter achievements")
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
        print("You can skip any field by pressing 'Enter'.")

        suspect_id = str(uuid.uuid4())  # Generate a unique identifier for each suspect

        ### Level 1 ###
        level_1 = {
            'name': cls.get_name_parts(),
            'nicknames': cls.get_multiple_inputs("Enter nickname")
        }

        ### Level 2 ###
        birthdate = cls.get_valid_date_parts()  # Take year, month, day separately
        level_2 = {
            'birthdate': birthdate.strftime("%Y-%m-%d") if birthdate else None,
            'special_dates': cls.get_multiple_inputs("Enter special date (e.g., marriage or achievement date)"),
            'phone_numbers': cls.get_multiple_inputs("Enter phone number (e.g., +1234567890)"),
            'vehicle_numbers': cls.get_multiple_inputs("Enter vehicle number"),
            'house_number': input("Enter house number (or press Enter to skip): ") or None,
            'special_identity_numbers': cls.get_multiple_inputs("Enter special identity number (e.g., roll number, emp number)")
        }

        ### Level 3 ###
        level_3 = {
            'email_addresses': cls.get_multiple_inputs("Enter email address"),
            'game_ids': cls.get_multiple_inputs("Enter game ID")
        }

        ### Level 4 ###
        level_4 = {
            'favorite_movies': cls.get_multiple_inputs("Enter favorite movie"),
            'favorite_sports': cls.get_multiple_inputs("Enter favorite sport"),
            'favorite_superstars': input("Enter favorite superstar or celebrity (or press Enter to skip): ") or None,
            'favorite_video_games': cls.get_multiple_inputs("Enter favorite video game"),
            'social_media_usernames': cls.get_multiple_inputs("Enter social media account username"),
            'favorite_singers': cls.get_multiple_inputs("Enter favorite singer"),
            'hobbies': cls.get_multiple_inputs("Enter hobbies"),
            'achievements': cls.get_multiple_inputs("Enter achievements"),
            'work_areas': cls.get_multiple_inputs("Enter work area (e.g., company name, school name, college name)")
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

######################################_Data_processing_################################################

        level_2_PD =[]
        
        cleandata=[]
        for i in level_2_values:
            value = re.sub('-','',i)
            cleandata.append(value)

        for i in cleandata:
            for length in range(1, len(i) + 1):  # Length from 1 to length of i
                for start in range(len(i) - length + 1):  # Starting index for the substring
                    substring = i[start:start + length]  # Get the substring of the specified length
                    if substring not in level_2_PD:  # Check if the substring is already in the list
                        level_2_PD.append(substring)

        file_name = 'processedData.json'
        data_to_store={
            "level_2_values":level_2_PD
        } 
        # Write the entire array to the file in JSON format
        with open(file_name, 'w') as file:
            json.dump(data_to_store, file)

            
######################################_Templates_################################################

        
  





if __name__ == "__main__":
    
    Alpha.target_Specification()
   # Alpha.suspect_Specification()
    Alpha.generator_Atom()
  

    # input_One = input("If you want to add target specifications, enter 'y': ")
    # input_Two = input("If you want to add suspect specifications, type 'suspect', otherwise type 'exit': ")
    # if input_Two.lower() == 'suspect':
    #     Alpha.suspect_Specification()
