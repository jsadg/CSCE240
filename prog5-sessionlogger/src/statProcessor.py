import re
from difflib import SequenceMatcher
class Processor:
    
    def __init__(self, file_name):
        #List of possible intents the user might be looking for
        self.intent_map = [
        ["business background"],
        ["business"],
        ["risk","troubles"],
        ["unresolved staff comments"],
        ["properties"],
        ["legal proceedings","lawsuits"],
        ["mine safety procedures"],
        ["financial information"],
        ["stocks"],
        ["financial conditions"],
        ["market risk"],
        ["financial statements"],
        ["accounting"],
        ["control procedures"],
        ["foreign jurisdiction"],
        ["executive information"],
        ["directors", "executives", "officers"],
        ["compensation"],
        ["security ownership"],
        ["director independence"],
        ["principal account"],
        ["exhibits"],
        ["financial schedule"],
        ["print all"]          
        ]
        #Gives the file to write to for this session
        self.file_name = file_name

    def identify_company(self, question):
        #Defaults to Campbell Soup
        company_name = "Campbell Soup"
        que_writer=open(self.file_name, "a")
        #Writes the question to the file
        que_writer.write("Your question was: "+question+"\n")
        que_writer.close()
        #Converts the question to all lowercase to be case insensitive
        question = question.lower()
        #Uses regular expressions to determine which company the user is referring to
        if(re.search(r".*camp( ?)bell.*", question)):
            company_name = "Campbell Soup"
        elif(re.search(r".*coin( ?)base.*", question)):
            company_name = "Coinbase"
        else:
            if(not self.handle_chit_chat(question)):
                que_writer.open(self.file_name, "a")
                #If neither RegEx matches, and not chit chat then the rest of the loop is skipped and the user is asked to try again
                que_writer.write("I do not know this information\n")
                que_writer.write("No company name detected, please try again\n\n")
                print("I do not know this information")
                print("No company name detected, please try again\n")
                que_writer.close()
            company_name = "Error"
        return company_name

    #Looks for the string in the intent map
    def find_in_intent_map(self, string):
        for x in range(len(self.intent_map)):
            for y in range(len(self.intent_map[x])):
                if self.intent_map[x][y]==string:
                    return [x,y]
        return 0


    #Given an x value from the map, appends the Part/Item number to an array and returns it
    def match_to_map(self, x):
        part = []
        match x:
            case 0:
                part.append("PART I")
                part.append("PART II")
            case 1:
                part.append("Item 1.")
                part.append("Item 1A.")
            case 2:
                part.append("Item 1A.")
                part.append("Item 1B.")
            case 3:
                part.append("Item 1B.")
                part.append("Item 2.")
            case 4:
                part.append("Item 2.")
                part.append("Item 3.")
            case 5:
                part.append("Item 3.")
                part.append("Item 4.")
            case 6:
                part.append("Item 4.")
                part.append("PART II") 
            case 7:
                part.append("PART II")
                part.append("PART III")  
            case 8:
                part.append("Item 5.")
                part.append("Item 6.")  
            case 9:
                part.append("Item 7.")
                part.append("Item 7A.")   
            case 10:
                part.append("Item 7A.")
                part.append("Item 8.")
            case 11:
                part.append("Item 8.")
                part.append("Item 9.")
            case 12:
                part.append("Item 9.")
                part.append("Item 9A.")
            case 13:
                part.append("Item 9A.")
                part.append("Item 9B.")
            case 14:
                part.append("Item 9C.")
                part.append("PART III")
            case 15:
                part.append("PART III")
                part.append("PART IV")               
            case 16:
                part.append("Item 10.")
                part.append("Item 11.")     
            case 17:
                part.append("Item 11.")
                part.append("Item 12.")        
            case 18:
                part.append("Item 12.")
                part.append("Item 13.")
            case 19:
                part.append("Item 13.")
                part.append("Item 14.")
            case 20:
                part.append("Item 14.")
                part.append("PART IV")
            case 21:
                part.append("PART IV")
                part.append("SIGNATURES")
            case 22:
                part.append("Item 15.")
                part.append("Item 16.")
            case 23:
                part.append("PART I")
                part.append("SIGNATURES")
        return part
                

    #Algorithm used to get a ratio for a partial match
    def simpson_coefficient(self, str1, str2):
        match = SequenceMatcher(None, str1, str2).find_longest_match()
        #Find the intersection between the lists
        denominator = min(len(str1), len(str2))
        if denominator == 0:
            return 0  #Avoid division by zero
        #Calculate the Simpson coefficient
        return (match.size / denominator)
    
    
        #Iterates through the intent map and uses simpson coefficient to find the closest match
    def match_question(self, question):
        max = 0
        matches = []
        for x in range(len(self.intent_map)):
            for y in range(len(self.intent_map[x])):
                #If the coefficient is greater then its a better match
                if(self.simpson_coefficient(self.intent_map[x][y],question)>max):
                    #Updates the value of max
                    max = self.simpson_coefficient(self.intent_map[x][y],question)
                    matches = []
                    matches.append([x,y])
                #If the coefficient is the same then the keyword is also stored in the matches array
                elif(self.simpson_coefficient(self.intent_map[x][y],question)==max):
                    matches.append([x,y])
        #Appends the max value to the front of the array to use for later 
        matches.insert(0, max)
        return self.check_threshold(matches)


    #Checks whether the threshold is successfully passed
    def check_threshold(self, match_array):
        if(match_array[0]>0.7):
            writer=open(self.file_name, "a")
            writer.write("Match ratio: "+str(match_array[0])+"\n")
            print("Match ratio: "+str(match_array[0])+"\n")
            writer.close()
            #If only match print out the result
            if(len(match_array) == 2):
                #Gets the x-value of the match-array
                return self.match_to_map(match_array[1][0])
            print("Which one of these were you looking for?")
            print("Type the exact statement you are looking that is listed below, or anything else to go back to the main page")
            for value in match_array[1:]:
                #Prints out each match
                print(self.intent_map[value[0]][value[1]])
            
            user_choice = input().lower()
            #Checks to see if the choice was possible before returning the data
            if self.check_matched(match_array,user_choice):
                return self.match_to_map(self.find_in_intent_map(user_choice)[0])
            else:
                #Otherwise exits from that menu
                return ["Exit"]
        else:            
            #Returns 0 if no match was high enough
            writer=open(self.file_name, "a")
            writer.write("Match ratio: "+str(match_array[0])+"\n")
            print("Match ratio: "+str(match_array[0]))
            writer.write("Match ratio was not high enough\n")
            writer.close()
            print("Match ratio was not high enough\n")
            return ["NoMatch"]
            
    #Identifies if a string is in the match array
    def check_matched(self, match_array, string):
        for match in match_array[1:]:
            #Returns true if the string was found in the match array
            if string == self.intent_map[match[0]][match[1]]:
                return True
        return False
    
    #Handles some basic chit chat
    def handle_chit_chat(self, question):
        writer=open(self.file_name, "a")
        if(self.simpson_coefficient(question,"hello")>0.8):
            writer.write("Hello!\n")
            print("Hello!")
            writer.close()
            return True
        elif(self.simpson_coefficient(question,"how is the weather?")>0.8):
            writer.write("The weather is nice!\n")
            print("The weather is nice!")
            writer.close()
            return True
        elif(self.simpson_coefficient(question,"how are you?")>0.8):
            writer.write("I'm doing well, but would do even better if you asked me a question\n")
            print("I'm doing well, but would do even better if you asked me a question")
            writer.close()
            return True
        #If no chit chat was detected then return false
        writer.close()
        return False
        
        
   