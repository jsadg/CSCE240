import re
import traceback

#Function to write the correct items/parts to the file
def print_to_file(start_item, end_item):
    #If option is changed to be zero than Campbell Soup is the selected company
    if option == 0:
        f = open("data/CampbellSoup2022.txt", "r")
        #File is opened then lines are skipped to get to the actual content of the file
        for _ in range(108):
            next(f)
    #If option is changed to be one than Coinbase is the selected company
    elif option == 1:
        f = open("data/Coinbase2022.txt", "r")
        #File is opened then lines are skipped to get to the actual content of the file
        for _ in range(193):
            next(f)
    ans_writer=open("data/output.txt", "a")
    print("Relevant information found\n")
    ans_writer.write("Here is the relevant text from "+company_name+"'s Form 10-K:\n\n")
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
                #Writes the line to the output.txt documents
                ans_writer.write(line)
    ans_writer.close()
    f.close()

#List of RegExs that handle user inputs, last letters are left off to allow some typos while
#still matching
#If a RegEx matches then print_to_file is called with the start and end of the part/item
#that the RegEx is meant to account for
def match_question(question):
    if re.search(r".*busines.*backgroun.*", question):
        print_to_file("PART I","PART II")
    elif re.search(r".*busines.*", question):
        print_to_file("Item 1.","Item 1A.")
    elif re.search(r".*risk( ?)facto.*", question):
        print_to_file("Item 1A.","Item 1B.")
    elif re.search(r".*unresolv.*staf", question):
        print_to_file("Item 1B.","Item 2.")
    elif re.search(r".*propertie.*", question):
        print_to_file("Item 2.","Item 3.")
    elif re.search(r".*lega.*procee.*", question):
        print_to_file("Item 3.","Item 4.")
    elif re.search(r".*mine.*safet.*procee.*", question):
        print_to_file("Item 4.","PART II")
    elif re.search(r".*finan.*informa.*", question):
        print_to_file("PART II","PART III")
    elif re.search(r".*stock.*", question):
        print_to_file("Item 5.","Item 6.")
        #Item 7 is reserved so no need to list it
    elif re.search(r".*finan.*conditi.*", question) or re.search(r".*resul.*operatio.*", question):
        print_to_file("Item 7.","Item 7A.")
    elif re.search(r".*marke.*risk.*", question):
        print_to_file("Item 7A.","Item 8.")
    elif re.search(r".*finan.*statemen.*", question):
        print_to_file("Item 8.","Item 9.")
    elif re.search(r".*chang.*accounti.*", question) or re.search(r".*[Dd]isagre.*[Aa]ccounti.*", question):
        print_to_file("Item 9.","Item 9A.")
    elif re.search(r".*contro.*procedur.*", question):
        print_to_file("Item 9A.","Item 9B.")
        #Item 9B is "Other informaiton" which is too general to write RegEx for
    elif re.search(r".*foreig.*jurisdi.*", question):
        print_to_file("Item 9C.","PART III")
    elif re.search(r".*executi.*informa.*", question):
        print_to_file("PART III","PART IV")
    elif re.search(r".*directo.*", question) or re.search(r".*executive.*", question) or re.search(r".*corporate.*", question):
        print_to_file("Item 10.","Item 11.")
    elif re.search(r".*compensat.*", question):
        print_to_file("Item 11.","Item 12.")
    elif re.search(r".*securit.*owner.*", question):
        print_to_file("Item 12.","Item 13.")
    elif re.search(r".*directo.*indep.*", question):
        print_to_file("Item 13.","Item 14.")
    elif re.search(r".*princip.*accoun.*", question):
        print_to_file("Item 14.","PART IV")
    elif re.search(r".*exhib.*", question):
        print_to_file("PART IV","SIGNATURES")
    elif re.search(r".*finan.*schedu.*", question):
        print_to_file("Item 15.","Item 16.")
        #Item 16 contains nothing
        #Command to print everything
    elif re.search(r".*print\sall.*", question):
        print_to_file("PART I","SIGNATURES")
    else:
        #If none of the RegExs matches than the user is told and asked to try again 
        que_writer=open("data/output.txt", "w")
        print("No information in the Form 10-k for "+company_name+" matches the request, please try again\n")
        que_writer.write("No information in the Form 10-k for the company matches the request, please try again")
        que_writer.close()    


#Start of program
over = False
option = 0
company_name=""
file_clear=open("data/output.txt", "w")
file_clear.close()

#Loop variable so that the program runs until the user stops it
while not over:
    try:
        print("Enter 0 to exit")
        print("Available companies: Coinbase, Campbell Soup")
        print("Enter in your question with the company name included:")
        question = input()
        #If the user inputs a zero then the while loop ends and the program stops running
        if question=="0":
            print("Goodbye")
            over = True
            break
        que_writer=open("data/output.txt", "w")
        #Writes the question to the output.txt file
        que_writer.write("Your question was: "+question+"\n")
        #Converts the question to all lowercase to be case insensitive
        question = question.lower()
        #Uses regular expressions to determine which company the user is referring to
        if(re.search(r".*camp( ?)bell( ?)soup.*", question)):
            option = 0
            company_name = "Campbell Soup"
        elif(re.search(r".*coin( ?)base.*", question)):
            option = 1
            company_name = "Coinbase"
        else:
            #If neither RegEx matches then the rest of the loop is skipped and the user is asked to try again
            que_writer.write("No company name detected, please try again")
            print("No company name detected, please try again\n")
            que_writer.close()
            continue
        que_writer.close()  
        #Calls the function to match RegExs
        match_question(question)


    except:
        #Handles any exceptions that might occur and tells the user to try again
        print("Invalid input, please try again\n")
        que_writer.write("Invalid input, please try again")       
        que_writer.close()