def inputText():
    print("Enter target info in text Combinational to stop write '$'")
    
    while True:
        data = input("Enter text : ")
        if data == "$":
            break
        with open("phase1/phase1Data/phase1TargetCombinationalDataInText.txt", "a") as file:
            file.write(data)
            file.write("\n")
    print("Enter target info in text Uncombinable to stop write '$'")
        
    while True:
        data = input("Enter text : ")
        if data == "$":
            break
        with open("phase1/phase1Data/phase1TargetUncombinableDataInText.txt", "a") as file:
            file.write(data)
            file.write("\n")
    
    
def inputNumber():
    print("Enter target info in number to stop write '$'")
    
    while True:
        data = input("Enter number : ")
        if data == "$":
            break
        with open("phase1/phase1Data/phase1TargetDataInNumber.txt", "a") as file :
            file.write(data)
            file.write("\n")

def phase1():
    inputText()
    inputNumber()
    
if __name__ == "__main__":
    phase1()