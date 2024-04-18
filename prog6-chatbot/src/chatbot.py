import statProcessor
import ui
import time
import sessionStatistics
import fileReader
import subprocess

class Main:
    #Looping condition
    over = False
    #Gets the time of start of the session and where to write to
    start_time = time.time()
    file_name = "chat_sessions/data_"+str(start_time)+".txt"
    #Creates the objects
    fileRead = fileReader.FileReader()
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
            elif company_name == "UsageStats":
                session_time = time.time() -start_time
                writer=open(file_name,"a")
                print("Session Statistics:")
                print("File Name:data_"+str(start_time)+".txt")
                print("#User Utterances:"+str(num_user_utter))
                print("#System Utterances:"+str(num_system_utter))
                print("Time Elapsed:"+str(session_time))
                writer.write("Session Statistics:\n")
                writer.write("File Name:data_"+str(start_time)+".txt\n")
                writer.write("#User Utterances:"+str(num_user_utter)+"\n")
                writer.write("#System Utterances:"+str(num_system_utter)+"\n")
                writer.write("Time Elapsed:"+str(session_time)+"\n")
                writer.close()
                continue
            elif company_name == "OtherStats":
                writer=open(file_name,"a")
                writer.write("Statistics Menu was Opened\n")
                writer.close()
                subprocess.run(["python3", "src/sessionStatistics.py"])
                writer=open(file_name,"a")
                writer.write("Statistics Menu was Closed\n\n")
                writer.close()
                continue
            #Calls the function to use string matching to find the part of the text the question relates to
            question = question.lower()
            part = []
            part = processor.match_question(question)
            writer=open(file_name,"a")
            #Checks for various flags set by the program
            if part[0] == "NoMatch":
                print("I do not know this information")
                print("Nothing in the Form 10-k for "+company_name+" matches the request, please try again\n")
                writer.write("I do not know this information\n")
                writer.write("No information in the Form 10-k for the company matches the request, please try again\n\n")
                writer.close()  
            elif part[0] == "Exit":
                print("You decided to exit\n")
                writer.write("You decided to exit\n")
                writer.close()
            elif part[0] == "information included":
                #Calls a method that prints out the relevant parts of the intent map
                processor.print_included_info()
            else:
                writer.close()
                #Used to get the updated 10-k folder
                print("Grabbing File, please be patient")
                fileRead.scrapeFile(company_name)
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
