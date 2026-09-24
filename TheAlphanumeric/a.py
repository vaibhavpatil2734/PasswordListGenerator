# TheAlphanumeric workflow
#
# Overall goal: generate a custom alphanumeric password list from target-specific
# text and numbers through four processing phases.
#
# phaseOne/inputData.py
# - inputText(): collects target-related text interactively and appends each entry
#   to phaseOne/inputData/targetDataInText.txt.
# - inputNumber(): collects target-related numbers interactively and appends each
#   entry to phaseOne/inputData/targetDataInNumber.txt.
#
# phaseTwo/inputComboGenerator.py
# - inputNumberComboGenerator(): reads the target numbers and generates contiguous
#   numeric substrings of at least two digits in
#   phaseTwo/comboGeneratedData/comboGeneratedDataNumber.txt.
# - inputTextComboGenerator(): reads the target text and generates word
#   combinations in phaseTwo/comboGeneratedData/comboGeneratedDataText.txt.
#
# phaseThree/TheGenerator.py
# - TheGenrator(): reads the text combinations and creates original, case-varied,
#   and symbol-substituted forms in phaseThree/row/rowText.txt.
#
# phaseFour/megaGenerator.py
# - generate_passwords(): combines text variants, number fragments, and symbols
#   into candidate passwords in
#   phaseFour/megaPasswordList/megaPasswordList.txt.
#
# Data files:
# - phaseOne/inputData/targetDataInText.txt stores the user's target text.
# - phaseOne/inputData/targetDataInNumber.txt stores the user's target numbers.
# - phaseTwo/comboGeneratedData/comboGeneratedDataText.txt stores generated text
#   combinations.
# - phaseTwo/comboGeneratedData/comboGeneratedDataNumber.txt stores generated
#   number combinations.
# - phaseThree/row/rowText.txt stores the transformed text variants.
# - phaseFour/megaPasswordList/megaPasswordList.txt stores the final password list.
#
# a.py documents the working files and their goals for this folder.
