from Alphanumeric.Alphanumeric import Alpha

def main():
    print("############################################")
    print("Greater data generates greater possibilities")
    print("############################################")

    print("# Select option Number #")
    try:
        operation = int(input("1. Alphanumeric 2. ...\n"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if operation == 1:
        Alpha.specification()
    else:
        print("Choose the correct option")

if __name__ == "__main__":
    main()
