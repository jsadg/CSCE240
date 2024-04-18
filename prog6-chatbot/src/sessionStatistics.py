import os
class SessionStats:
    
    #Appends the stats to the end of a chat session file
    def append_stats(self,file_name,start_time,num_user_utter,num_system_utter,session_time):
        writer=open(file_name, "a")
        print("Session Statistics:")
        print("File Name:data_"+str(start_time)+".txt")
        print("#User Utterances:"+str(num_user_utter))
        print("#System Utterances:"+str(num_system_utter))
        print("Time Elapsed:"+str(session_time))
        writer.write("\n")
        writer.write("Session Statistics:\n")
        writer.write("File Name:data_"+str(start_time)+".txt\n")
        writer.write("#User Utterances:"+str(num_user_utter)+"\n")
        writer.write("#System Utterances:"+str(num_system_utter)+"\n")
        writer.write("Time Elapsed:"+str(session_time)+"\n")
        writer.close()
        
    def update_csv(self):
        #Gets the files
        files = [f for f in os.listdir("chat_sessions")]
        #Gets chronological order
        list.sort(files)
        writer=open("data/chat_statistics.csv", "w")
        #Writes the header of the csv file
        writer.write("Serial#,Chat_File,#User_Utterance,#System_Utterance,Time_Taken\n")
        serial_num=1
        for file in files:
            text=open("chat_sessions/"+file,'r').read().split('\n')
            try:
                if text[-6] != "Session Statistics:":
                    continue
            except IndexError:
                continue
            #Adds the serial number to the csv
            writer.write(str(serial_num)+",")
            #Adds the information at the end of each file to the chat statistics part
            for i in range(-5, -2, 1):
                writer.write(text[i].split(":")[1]+",")
            #Adds the newline to the last part of it
            writer.write(text[-2].split(":")[1]+"\n")     
            #Updates the serial number       
            serial_num+=1

    #Method to get all of the information in the csv file
    def get_total_summary(self):
        text=open("data/chat_statistics.csv",'r').read().split('\n')
        total_chats = 0
        total_user_utters = 0
        total_system_utters = 0
        total_time = 0
        #Gets the total amount of stats by parsing through the csv file
        for line in text[1:len(text)-1]:
            data=line.split(",")
            total_chats+=1
            total_user_utters+=int(data[2])
            total_system_utters+=int(data[3])
            total_time+=float(data[4])
        print("Total Summary:")
        print("Number of chats: "+str(total_chats))
        print("Number of user utterances: "+str(total_user_utters))
        print("Number of system utterances: "+str(total_system_utters))
        print("Total Time: "+str(total_time)+" seconds")
        
    def get_specific_summary(self,number):
        text=open("data/chat_statistics.csv",'r').read().split('\n')
        #Gets the stats by parsing through the csv file
        number = int(number)
        if(number>len(text)-2 or number <= 0):
            print("There are only "+str(len(text)-2)+" valid chat sessions, choose a valid number next time")
            return
        line=text[number]
        data=line.split(",")
        print("Chat "+str(number)+":")
        print("Number of user utterances: "+data[2])
        print("Number of system utterances: "+data[3])
        print("Time Taken: " + data[4])
  
    #Prints the given chat number to the console
    def print_chat(self,number):
        text=open("data/chat_statistics.csv",'r').read().split('\n')
        #Gets the file name by parsing through the csv file
        number = int(number)
        if(number>len(text)-2 or number <= 0):
            print("There are only "+str(len(text)-2)+" valid chat sessions, choose a valid number next time")
            return    
        line=text[number]
        data=line.split(",")      
        file = open("chat_sessions/"+data[1])
        print("")
        for line in file:
            print(line,end="")

    #Used to run the program
    def run(self):
        over = False
        self.update_csv()
        while(not over):
            try:
                #Option selection to use the session stats getter
                print("Welcome to the chat summary menu")
                print("Enter 0 to quit")
                print("Enter 1 to view a summary of all the sessions")
                print("Enter 2 to view a specific session summary")
                print("Enter 3 to view a chat")
                print("Enter 4 to update the chat_statistics.csv file")
                choice = input()
                if choice == "0":
                    print("Statistics Menu Closed\n")
                    over = True
                    break
                if choice == "1":
                    self.get_total_summary()
                elif choice == "2":
                    print("Enter the number of the chat you wish to summarize")
                    num_chat=input()
                    self.get_specific_summary(num_chat)
                elif choice == "3":
                    print("Enter the number of the chat you wish to view")
                    num_chat=input()
                    self.print_chat(num_chat)    
                elif choice == "4":
                    self.update_csv()
                    print("chat_statistics.csv updated")
                    
                else:
                    print("You did not select a valid option")     
                    
            except:
                print("An error has occured please try again")



#Code that executes when file is ran
if __name__ == "__main__":
    start=SessionStats()
    start.run()
