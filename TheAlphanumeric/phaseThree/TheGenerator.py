import os

def TheGenrator():
    input_path = os.path.join("TheAlphanumeric", "phaseTwo", "comboGeneratedData", "comboGeneratedDataText.txt")
    output_path = os.path.join(os.path.dirname(__file__), "TheAlphanumeric", "phaseThree", "inputData", "formattedOutput.txt")

    with open(input_path, "r") as infile:
        lines = infile.readlines()

    with open(output_path, "w") as outfile:
        for line in lines:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            # 1. Title Case
            title_case = line.title()

            # 2. UPPERCASE
            upper_case = line.upper()

            # 3. Sentence case (only first letter capital)
            sentence_case = line.capitalize()

            # 4. firstWordLowerRestCapital (e.g., "first Word Capitalized")
            words = line.split()
            if words:
                custom_case = words[0].lower() + ' ' + ' '.join(word.capitalize() for word in words[1:])
            else:
                custom_case = ""

            # Write all versions to the new file
            outfile.write(f"Original: {line}\n")
            outfile.write(f"Title Case: {title_case}\n")
            outfile.write(f"UPPERCASE: {upper_case}\n")
            outfile.write(f"Sentence Case: {sentence_case}\n")
            outfile.write(f"Custom Case: {custom_case}\n")
            outfile.write("-" * 40 + "\n")  # separator for readability

if __name__ == "__main__":
    TheGenrator()
