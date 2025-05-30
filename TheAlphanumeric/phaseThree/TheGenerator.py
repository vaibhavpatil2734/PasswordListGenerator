import os

def TheGenrator():
        input_path = os.path.join("TheAlphanumeric", "phaseTwo", "comboGeneratedData", "comboGeneratedDataText.txt")
        output_path = os.path.join(os.path.dirname(__file__), "TheAlphanumeric", "phaseThree", "inputData", "targetDataInNumber.txt")

        while True:
            with open(input_path,"r")as file:
                line = file.readline().strip()
                print(line)
            
if __name__=="__main__":
    TheGenrator()
    