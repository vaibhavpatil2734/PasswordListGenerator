import os

def TheGenrator():
    input_path = os.path.join("TheAlphanumeric", "phaseTwo", "comboGeneratedData", "comboGeneratedDataText.txt")
    output_path = os.path.join("TheAlphanumeric", "phaseThree", "row", "rowText.txt")

    with open(input_path, "r") as infile:
        lines = infile.readlines()

    with open(output_path, "w") as outfile:
        for line in lines:
            line = line.strip()
            if not line:
                continue

            words = line.split()
            # Always write original
            outfile.write(f"{line}\n")
            
            # Only write custom_case if more than 1 word
            if len(words) > 1:
                custom_case = words[0].lower() + ' ' + ' '.join(word.capitalize() for word in words[1:])
                outfile.write(f"{custom_case}\n")

            # Always write title case and upper case
            outfile.write(f"{line.title()}\n")
            outfile.write(f"{line.upper()}\n")

            # Only write sentence case if more than 1 word
            if len(words) > 1:
                outfile.write(f"{line.capitalize()}\n")

if __name__ == "__main__":
    TheGenrator()
