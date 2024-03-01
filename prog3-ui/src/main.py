import statProcessor
import ui

class Main:
    #Clears the file
    file_clear=open("data/output.txt", "w")
    file_clear.close()
    #Looping condition
    over = False
    ui = ui.Ui()
    processor = statProcessor.Processor()
    #Loop variable so that the program runs until the user stops it
    while not over:
        try:
            question = ui.ask_question()
            if question.lower()=="quit" or question.lower()=="q":
                print("Goodbye")
                over = True
                break
            
            #Identifies the company's name
            company_name = processor.identify_company(question)
            #If the company name was not identified then restarts the loop
            if company_name == "Error":
                continue
            
            #Calls the function to match RegExs to find the part of the text the question relates to
            part = []
            part = processor.match_question(question)
            if part[0] == "NoMatch":
                que_writer=open("data/output.txt", "a")
                print("I do not know this information")
                print("Nothing in the Form 10-k for "+company_name+" matches the request, please try again\n")
                que_writer.write("I do not know this information\n")
                que_writer.write("No information in the Form 10-k for the company matches the request, please try again\n\n")
                que_writer.close()  
            else:
                ui.print_to_file(company_name,part[0],part[1])
        except:
            #Handles any exceptions that might occur and tells the user to try again
            que_writer=open("data/output.txt", "a")
            print("Invalid input, please try again\n")
            que_writer.write("Invalid input, please try again\n")       
            que_writer.close()
            over = True