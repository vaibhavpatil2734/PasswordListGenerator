import os
from itertools import combinations, permutations


# Get the directory where this Python file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def inputNumberComboGenerator():
    input_path = os.path.join(
        BASE_DIR,
        "..",
        "phase1",
        "phase1Data",
        "phase1TargetDataInNumber.txt"
    )

    output_path = os.path.join(
        BASE_DIR,
        "phase2Data",
        "phase2ComboGeneratedDataNumber.txt"
    )

    with open(input_path, "r") as f, open(output_path, "a") as file:
        while True:
            number = f.readline().strip()

            if not number:  # End of file or empty line
                break

            length = len(number)

            for i in range(length):
                for j in range(i + 2, length + 1):
                    # Generate at least 2-digit combinations
                    file.write(number[i:j] + "\n")


def inputTextComboGenerator():
    input_path = os.path.join(
        BASE_DIR,
        "..",
        "phase1",
        "phase1Data",
        "phase1TargetCombinationalDataInText.txt"
    )

    output_path = os.path.join(
        BASE_DIR,
        "phase2Data",
        "phase2ComboGeneratedDataText.txt"
    )

    with open(input_path, "r", encoding="utf-8") as f, \
         open(output_path, "a", encoding="utf-8") as file:

        for line in f:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            words = line.split()
            length = len(words)

            generated = set()


            for r in range(1, length + 1):

                # Select r words from the current input line
                for selected_words in combinations(words, r):

                    # Change their order in every possible way
                    for combo in permutations(selected_words):

                        result = " ".join(combo)

                        if result not in generated:
                            file.write(result + "\n")
                            generated.add(result)

            # Keep each original input line isolated
            file.write("\n")

def phase2():
    inputNumberComboGenerator()
    inputTextComboGenerator()


if __name__ == "__main__":
    phase2()