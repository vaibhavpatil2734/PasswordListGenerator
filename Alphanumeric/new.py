list = []
names = []
temp_names = []
phoneNo = ''

# Getting Date of Birth in correct format
dob = input("Date of birth (DDMMYYYY): ")
if len(dob) == 8:
    day = dob[:2]
    month = dob[2:4]
    year = dob[4:]
else:
    print("Wrong format for DOB, make sure it is 8 numbers in DDMMYYYY")
    exit()

# Getting phone number input
phoneNo = input("Enter phone number: ")

# Function to input important words
def ListOfImportantWords():
    print("Please provide the following details:")
    names.append(input("First name: "))
    names.append(input("Surname: "))
    names.append(input("Nickname: "))
    print("\n")
    names.append(input("Partner's name: "))
    names.append(input("Partner's Nickname: "))
    print("\n")
    names.append(input("Pet's name: "))
    names.append(input("Company name: "))
    print("\n")
    names.append(input("Child's name: "))
    names.append(input("Child's nickname: "))
    print("\n")
    names.append(input("City: "))
    names.append(input("Country: "))
    names.append(input("Favourite colour: "))
    print("\nEnter all other keywords (press Enter twice to finish):")
    
    # Taking multiple other keywords from user
    while True:
        inp = input()
        if inp == '':
            break
        names.append(inp)

    # Remove empty strings from names
    while '' in names: 
        names.remove('')

# Function to generate permutations of word with upper and lower case combinations
def permute(inp):
    n = len(inp)
    mx = 1 << n
    inp = inp.lower()
    
    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if ((i >> j) & 1) == 1:
                combination[j] = inp[j].upper()
        temp = ""
        for char in combination:
            temp += char
        temp_names.append(temp)

# Function to create wordlist using names and important information
def WordListCreator(list):
    for word in names:
        for i in range(0, len(word) + 1):
            list.append(word[:i] + day + word[i:])
            list.append(word[:i] + month + word[i:])
            list.append(word[:i] + year + word[i:])
            if len(year) == 4:
                list.append(word[:i] + year[2:] + word[i:])
            list.append(word[:i] + phoneNo + word[i:])
    
    # Adding the phone number itself to the wordlist if available
    if phoneNo:
        list.append(phoneNo)

# Function to write the wordlist to a file
def WriteToFile(list):
    with open('wordlist.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)

# Main block to call functions sequentially
if __name__ == "__main__":
    ListOfImportantWords()  # Gather important words and names
    for name in names:
        permute(name)        # Generate permutations of each name
    names = names + temp_names  # Combine original names with permutations
    WordListCreator(list)    # Create the final wordlist
    WriteToFile(list)        # Write the wordlist to a file
    print("Wordlist has been successfully generated and saved to 'wordlist.txt'")
