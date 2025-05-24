import os
from itertools import combinations

def inputNumberComboGenerator():
    input_path = os.path.join(os.path.dirname(__file__), "..", "phaseOne", "inputData", "targetDataInNumber.txt")
    output_path = os.path.join("TheAlphanumeric", "phaseTwo", "comboGeneratedData", "comboGeneratedDataNumber.txt")

    with open(input_path, "r") as f, open(output_path, "a") as file:
        while True:
            number = f.readline().strip()
            if not number:  # End of file or empty line
                break

            length = len(number)
            for i in range(length):
                for j in range(i + 2, length + 1):  # At least 2-digit substrings
                    file.write(number[i:j] + "\n")
            
        
def inputTextComboGenerator():
    input_path = os.path.join(os.path.dirname(__file__), "..", "phaseOne", "inputData", "targetDataInText.txt")
    output_path = os.path.join("TheAlphanumeric", "phaseTwo", "comboGeneratedData", "comboGeneratedDataText.txt")

    with open(input_path, "r") as f, open(output_path, "a") as file:
        while True:
            line = f.readline().strip()
            if not line:
                break

            words = line.split()
            length = len(words)

            # Generate combinations of all lengths (1 to len)
            for r in range(1, length + 1):
                for combo in combinations(words, r):
                    file.write(" ".join(combo) + "\n")
                    
                    
                    
if __name__ == "__main__":
    inputNumberComboGenerator()
    inputTextComboGenerator()