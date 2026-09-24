import os
import itertools


# Get the directory where this Python file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_symbol_variants_with_spaces(text):
    substitutions = {
        'a': ['@'],
        'i': ['!'],
        'o': ['0'],
        's': ['$']
    }

    positions = [(i, substitutions[c]) for i, c in enumerate(text) if c in substitutions]

    if not positions:
        return []

    variants = set()
    num_positions = len(positions)

    for r in range(1, num_positions + 1):
        for combo in itertools.combinations(positions, r):
            indexes, choice_groups = zip(*combo)
            for replacements in itertools.product(*choice_groups):
                chars = list(text)
                for idx, sub in zip(indexes, replacements):
                    chars[idx] = sub
                variants.add("".join(chars))

    return sorted(variants)


def TheGenrator():
    input_path = os.path.join(
        BASE_DIR,
        "..",
        "phase2",
        "phase2Data",
        "phase2ComboGeneratedDataText.txt"
    )

    output_path = os.path.join(
        BASE_DIR,
        "phase3Data",
        "phase3SubtitutedDataText.txt"
    )

    with open(input_path, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    with open(output_path, "w", encoding="utf-8") as outfile:
        for line in lines:
            line = line.strip()
            if not line:
                continue

            words = line.split()
            outfile.write(f"{line}\n")  # Original

            if len(words) > 1:
                custom_case = words[0].lower() + ' ' + ' '.join(word.capitalize() for word in words[1:])
                outfile.write(f"{custom_case}\n")

            outfile.write(f"{line.title()}\n")   # Title Case
            outfile.write(f"{line.upper()}\n")   # Upper Case

            if len(words) > 1:
                outfile.write(f"{line.capitalize()}\n")  # Sentence Case

            for variant in get_symbol_variants_with_spaces(line.lower()):
                outfile.write(f"{variant}\n")

def phase3():
    TheGenrator()


if __name__ == "__main__":
    phase3()