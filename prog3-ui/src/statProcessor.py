import re
class Processor:

    def identify_company(self, question):
        #Defaults to Campbell Soup
        company_name = "Campbell Soup"
        que_writer=open("data/output.txt", "a")
        #Writes the question to the output.txt file
        que_writer.write("Your question was: "+question+"\n")
        #Converts the question to all lowercase to be case insensitive
        question = question.lower()
        #Uses regular expressions to determine which company the user is referring to
        if(re.search(r".*camp( ?)bell.*", question)):
            company_name = "Campbell Soup"
        elif(re.search(r".*coin( ?)base.*", question)):
            company_name = "Coinbase"
        else:
            #If neither RegEx matches then the rest of the loop is skipped and the user is asked to try again
            que_writer.write("I do not know this information\n")
            que_writer.write("No company name detected, please try again\n\n")
            print("I do not know this information")
            print("No company name detected, please try again\n")
            company_name = "Error"
        que_writer.close()
        return company_name


    #List of RegExs that handle user inputs, last letters are left off to allow some typos while
    #still matching
    # If a regex matches than the start and end of it it placed in the part array
    def match_question(self, question):
        question = question.lower()
        part = []
        if re.search(r".*busines.*backgroun.*", question):
            part.append("PART I")
            part.append("PART II")
        elif re.search(r".*busines.*", question):
            part.append("Item 1.")
            part.append("Item 1A.")
            #Accounts for more specific query
        elif re.search(r".*risk*", question) and not re.search(r".*marke.*risk.*", question):
            part.append("Item 1A.")
            part.append("Item 1B.")
        elif re.search(r".*unresolv.*staf", question):
            part.append("Item 1B.")
            part.append("Item 2.")
        elif re.search(r".*propertie.*", question):
            part.append("Item 2.")
            part.append("Item 3.")
        elif re.search(r".*lega.*procee.*", question):
            part.append("Item 3.")
            part.append("Item 4.")
        elif re.search(r".*mine.*safet.*", question):
            part.append("Item 4.")
            part.append("PART II")
        elif re.search(r".*finan.*informa.*", question):
            part.append("PART II")
            part.append("PART III")            
        elif re.search(r".*stock.*", question):
            part.append("Item 5.")
            part.append("Item 6.")            
        #Item 7 is reserved so no need to list it
        elif re.search(r".*finan.*conditi.*", question) or re.search(r".*resul.*operatio.*", question):
            part.append("Item 7.")
            part.append("Item 7A.")  
        elif re.search(r".*marke.*risk.*", question):
            part.append("Item 7A.")
            part.append("Item 8.")
        elif re.search(r".*finan.*statemen.*", question):
            part.append("Item 8.")
            part.append("Item 9.")
        elif re.search(r".*chang.*accounti.*", question) or re.search(r".*[Dd]isagre.*[Aa]ccounti.*", question):
            part.append("Item 9.")
            part.append("Item 9A.")
        elif re.search(r".*contro.*procedur.*", question):
            part.append("Item 9A.")
            part.append("Item 9B.")
        #Item 9B is "Other informaiton" which is too general to write RegEx for
        elif re.search(r".*foreig.*jurisdi.*", question):
            part.append("Item 9C.")
            part.append("PART III")
        elif re.search(r".*executi.*informa.*", question):
            part.append("PART III")
            part.append("PART IV")
        elif re.search(r".*directo.*", question) or re.search(r".*executive.*", question) or re.search(r".*corporate.*", question) and not re.search(r".*directo.*indep.*", question):
            part.append("Item 10.")
            part.append("Item 11.")
        elif re.search(r".*compensat.*", question):
            part.append("Item 11.")
            part.append("Item 12.")
        elif re.search(r".*securit.*owner.*", question):
            part.append("Item 12.")
            part.append("Item 13.")
        elif re.search(r".*directo.*indep.*", question):
            part.append("Item 13.")
            part.append("Item 14.")
        elif re.search(r".*princip.*accoun.*", question):
            part.append("Item 14.")
            part.append("PART IV")
        elif re.search(r".*exhib.*", question):
            part.append("PART IV")
            part.append("SIGNATURES")
        elif re.search(r".*finan.*schedu.*", question):
            part.append("Item 15.")
            part.append("Item 16.")
        #Item 16 contains nothing
        #Command to print everything
        elif re.search(r".*print(\s)?all.*", question):
            part.append("PART I")
            part.append("SIGNATURES")
        else:
            #If there is no match then it return a single length array with "NoMatch"
            part.append("NoMatch")
        return part