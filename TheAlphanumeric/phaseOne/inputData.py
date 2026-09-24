def inputText():
    print("Enter target info in text Combinational to stop write '$'")
    
    while True:
        data = input("Enter text : ")
        if data == "$":
            break
        with open("inputData/targetCombinationalDataInText.txt", "a") as file:
            file.write(data)
            file.write("\n")
    print("Enter target info in text Uncombinable to stop write '$'")
        
    while True:
        data = input("Enter text : ")
        if data == "$":
            break
        with open("inputData/targetUncombinableDataInText.txt", "a") as file:
            file.write(data)
            file.write("\n")
    
    
def inputNumber():
    print("Enter target info in number to stop write '$'")
    
    while True:
        data = input("Enter number : ")
        if data == "$":
            break
        with open("inputData/targetDataInNumber.txt", "a") as file :
            file.write(data)
            file.write("\n")
    
if __name__ == "__main__":
    inputText()
    inputNumber()