import os

def generate_passwords():
    input_path_number = os.path.join("TheAlphanumeric", "phaseTwo", "comboGeneratedData", "comboGeneratedDataNumber.txt")
    input_path_string = os.path.join(os.path.dirname(__file__), "..", "phaseThree", "row", "rowText.txt")
    output_path = os.path.join("TheAlphanumeric", "phaseFour", "megaPasswordList", "megaPasswordList.txt")

    symbols = ['@', '#', '$', '!', '_', '-', '.', '*']

    with open(input_path_string, "r", encoding="utf-8") as string_file:
        strings = [line.strip() for line in string_file if line.strip()]

    with open(input_path_number, "r", encoding="utf-8") as number_file:
        numbers = [line.strip() for line in number_file if line.strip()]

    pair_count = min(len(strings), len(numbers))

    with open(output_path, "w", encoding="utf-8") as output_file:
        for i in range(pair_count):
            string = strings[i]
            number = numbers[i]

            for symbol in symbols:
                output_file.write(string + "\n")
                output_file.write(number + "\n")
                output_file.write(symbol + "\n")
                output_file.write(string + symbol + "\n")
                output_file.write(string + number + "\n")
                output_file.write(symbol + string + "\n")
                output_file.write(symbol + number + "\n")
                output_file.write(number + string + "\n")
                output_file.write(number + symbol + "\n")
                output_file.write(string + string + "\n")
                output_file.write(symbol + symbol + "\n")
                output_file.write(number + number + "\n")
                output_file.write(string + symbol + number + "\n")
                output_file.write(string + number + symbol + "\n")
                output_file.write(symbol + string + number + "\n")
                output_file.write(symbol + number + string + "\n")
                output_file.write(number + string + symbol + "\n")
                output_file.write(number + symbol + string + "\n")
                output_file.write(string + string + string + "\n")
                output_file.write(symbol + symbol + symbol + "\n")
                output_file.write(number + number + number + "\n")
                output_file.write(string + string + symbol + "\n")
                output_file.write(string + string + number + "\n")
                output_file.write(string + symbol + string + "\n")
                output_file.write(string + number + string + "\n")
                output_file.write(symbol + symbol + string + "\n")
                output_file.write(symbol + symbol + number + "\n")
                output_file.write(symbol + string + symbol + "\n")
                output_file.write(symbol + number + symbol + "\n")
                output_file.write(number + number + string + "\n")
                output_file.write(number + number + symbol + "\n")
                output_file.write(number + string + number + "\n")
                output_file.write(number + symbol + number + "\n")
                output_file.write(string + symbol + symbol + "\n")
                output_file.write(string + number + number + "\n")
                output_file.write(symbol + string + string + "\n")
                output_file.write(symbol + number + number + "\n")
                output_file.write(number + symbol + symbol + "\n")

if __name__ == "__main__":
    generate_passwords()
