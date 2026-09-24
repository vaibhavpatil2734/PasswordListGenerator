import os


def generate_passwords():

    # Base directory = TheAlphanumeric
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Input paths
    input_path_number = os.path.join(
        BASE_DIR,
        "phase2",
        "phase2Data",
        "phase2ComboGeneratedDataNumber.txt"
    )

    input_path_string = os.path.join(
        BASE_DIR,
        "phase3",
        "phase3Data",
        "phase3SubtitutedDataText.txt"
    )

    # Output directory
    output_dir = os.path.join(
        BASE_DIR,
        "phase4",
        "phase4Data"
    )

    # Output file
    output_path = os.path.join(
        output_dir,
        "megaPasswordList.txt"
    )

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    symbols = ['@', '#', '$', '!', '_', '-', '.', '*']

    # Read strings
    with open(input_path_string, "r", encoding="utf-8") as string_file:
        raw_strings = [
            line.strip()
            for line in string_file
            if line.strip()
        ]

    # Read numbers
    with open(input_path_number, "r", encoding="utf-8") as number_file:
        numbers = [
            line.strip()
            for line in number_file
            if line.strip()
        ]

    # Generate string variants
    string_variants = []

    for raw in raw_strings:
        string_variants.append(raw)

        if " " in raw:
            string_variants.append(raw.replace(" ", ""))
            string_variants.append(raw.replace(" ", "_"))
            string_variants.append(raw.replace(" ", "-"))

    # Generate passwords
    with open(output_path, "w", encoding="utf-8") as output_file:

        for string in string_variants:

            for number in numbers:

                for symbol in symbols:

                    # ============================================================
                    # HIGH POSSIBILITY
                    # ============================================================

                    output_file.write(string + "\n")
                    output_file.write(number + "\n")

                    output_file.write(string + number + "\n")
                    output_file.write(string + symbol + "\n")

                    output_file.write(number + string + "\n")
                    output_file.write(symbol + string + "\n")

                    output_file.write(string + symbol + number + "\n")
                    output_file.write(string + number + symbol + "\n")

                    output_file.write(string + string + "\n")
                    output_file.write(string + string + number + "\n")
                    output_file.write(string + string + symbol + "\n")

                    output_file.write(string + number + number + "\n")
                    output_file.write(string + symbol + symbol + "\n")


                    # ============================================================
                    # MEDIUM POSSIBILITY
                    # ============================================================

                    # output_file.write(number + string + symbol + "\n")
                    # output_file.write(number + symbol + string + "\n")

                    # output_file.write(symbol + string + number + "\n")
                    # output_file.write(symbol + number + string + "\n")

                    # output_file.write(string + number + string + "\n")
                    # output_file.write(string + symbol + string + "\n")

                    # output_file.write(string + string + string + "\n")

                    # output_file.write(number + number + string + "\n")
                    # output_file.write(number + number + symbol + "\n")

                    # output_file.write(symbol + symbol + string + "\n")
                    # output_file.write(symbol + symbol + number + "\n")

                    # output_file.write(number + string + number + "\n")
                    # output_file.write(number + symbol + number + "\n")


                    # ============================================================
                    # LOW POSSIBILITY
                    # ============================================================

                    # output_file.write(symbol + "\n")

                    # output_file.write(number + symbol + "\n")
                    # output_file.write(symbol + number + "\n")

                    # output_file.write(number + number + "\n")
                    # output_file.write(symbol + symbol + "\n")

                    # output_file.write(number + number + number + "\n")
                    # output_file.write(symbol + symbol + symbol + "\n")

                    # output_file.write(symbol + string + string + "\n")
                    # output_file.write(symbol + number + number + "\n")

                    # output_file.write(number + symbol + symbol + "\n")
                    # output_file.write(symbol + number + symbol + "\n")

                    # output_file.write(number + number + symbol + "\n")
                    # output_file.write(symbol + symbol + number + "\n")

def phase4():
    generate_passwords()

if __name__ == "__main__":
    phase4()