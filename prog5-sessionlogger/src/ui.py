import re
class Ui:
    
    def __init__(self, file_name):
        #Gives the file to write to for this session
        self.file_name = file_name

    #Asks the user to enter in a question and then returns it
    def ask_question(self):
        print("Enter quit or q to exit")
        print("Available companies: Coinbase, Campbell Soup")
        print("Enter in your question with the company name included:")
        question = input()
        return question
    
    #Function to write the correct items/parts to the file
    def print_to_file(self, company, start_item, end_item):
        if company == "Campbell Soup":
            f = open("data/CampbellSoup2022.txt", "r")
            #File is opened then lines are skipped to get to the actual content of the file
            for _ in range(108):
                next(f)
        #If option is changed to be one than Coinbase is the selected company
        elif company == "Coinbase":
            f = open("data/Coinbase2022.txt", "r")
            #File is opened then lines are skipped to get to the actual content of the file
            for _ in range(193):
                next(f)
        ans_writer=open(self.file_name, "a")
        print("Relevant information found, "+self.file_name+" updated\n")
        ans_writer.write("Here is the relevant text from "+company+"'s Form 10-K:\n")
        included = False
        for line in f:
            #If the inputted start string is in the line then included is changed to true
            if start_item in line: 
                included = True
            #If the inputted end string is in the line then the for loop is broken out of          
            if end_item in line:
                break
            if included:
                #If included is true then all the lines are after the start string
                #Table of Contents and number lines are excluded to condense relevant data
                if "Table of Contents" not in line and not re.search(r"^\d+$", line):
                    #Writes the line to the documents
                    ans_writer.write(line)
        ans_writer.write("\n")
        ans_writer.close()
        f.close()