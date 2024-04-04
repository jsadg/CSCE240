import statProcessor
import ui
import time
import sessionStatistics
class Main:
    #Looping condition
    over = False
    #Gets the time of start of the session and where to write to
    start_time = time.time()
    file_name = "chat_sessions/data_"+str(start_time)+".txt"
    #Creates the objects
    ui = ui.Ui(file_name)
    processor = statProcessor.Processor(file_name)
    stats = sessionStatistics.SessionStats()
    #Instantiates the number of utterances, system is set to one for greeting
    num_user_utter = 0  
    num_system_utter = 1
    #Loop variable so that the program runs until the user stops it
    while not over:
        try:
            question = ui.ask_question()
            num_user_utter+=1
            num_system_utter+=1
            if question.lower()=="quit" or question.lower()=="q":
                writer=open(file_name, "a")
                writer.write("Your question was: "+question+"\n")
                writer.write("You decided to quit\n")                
                print("Goodbye")
                writer.close()
                over = True
                break
            
            #Identifies the company's name
            company_name = processor.identify_company(question)
            #If the company name was not identified then restarts the loop
            if company_name == "Error":
                continue
            
            #Calls the function to use string matching to find the part of the text the question relates to
            part = []
            part = processor.match_question(question)
            if part[0] == "NoMatch":
                writer=open(file_name, "a")
                print("I do not know this information")
                print("Nothing in the Form 10-k for "+company_name+" matches the request, please try again\n")
                writer.write("I do not know this information\n")
                writer.write("No information in the Form 10-k for the company matches the request, please try again\n\n")
                writer.close()  
            elif part[0] == "Exit":
                writer=open(file_name, "a")
                print("You decided to exit\n")
                writer.write("You decided to exit\n")
                writer.close()
            else:
                ui.print_to_file(company_name,part[0],part[1])
        except:
            #Handles any exceptions that might occur and tells the user to try again
            writer=open(file_name, "a")
            print("Invalid input, please try again\n")
            writer.write("Invalid input, please try again\n")       
            writer.close()
    #Prints the session statistics
    end_time = time.time()
    session_time = end_time-start_time
    
    stats.append_stats(file_name,start_time,num_user_utter,num_system_utter,session_time)
