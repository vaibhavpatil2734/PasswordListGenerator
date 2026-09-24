import os
from itertools import combinations, permutations


# Get the directory where this Python file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def inputNumberComboGenerator():
    input_path = os.path.join(
        BASE_DIR,
        "..",
        "phaseOne",
        "inputData",
        "targetDataInNumber.txt"
    )

    output_path = os.path.join(
        BASE_DIR,
        "comboGeneratedData",
        "comboGeneratedDataNumber.txt"
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
        "phaseOne",
        "inputData",
        "targetCombinationalDataInText.txt"
    )

    output_path = os.path.join(
        BASE_DIR,
        "comboGeneratedData",
        "comboGeneratedDataText.txt"
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

            # Generate all possible combinations
            # with all possible word orders.
            #
            # Example:
            # vaibhav ramchandra patil
            #
            # vaibhav
            # ramchandra
            # patil
            #
            # vaibhav ramchandra
            # ramchandra vaibhav
            # vaibhav patil
            # patil vaibhav
            # ramchandra patil
            # patil ramchandra
            #
            # vaibhav ramchandra patil
            # vaibhav patil ramchandra
            # ramchandra vaibhav patil
            # ramchandra patil vaibhav
            # patil vaibhav ramchandra
            # patil ramchandra vaibhav

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


if __name__ == "__main__":
    inputNumberComboGenerator()
    inputTextComboGenerator()