#include <iostream>
#include <fstream>
#include <string>
#include "Headers/GmailHeader.h"
#include "Headers/OutlookHeader.h"
#include "Headers/EmailInformationExtractor.h"

int main(){
    bool over = false;
    std::string headerFileName = "";
    std::string firstLine = "";
    std::string partName = "";
    GmailHeader gmail;
    OutlookHeader outlook;
    while(!over){
        try{
            std::cout << "Enter the name of header file you want to read from or 0 to quit" << std::endl;
            std::cin >> headerFileName;
            //If the user enters 0 they quit
            if (headerFileName == "0"){
                over = true;
                break;
            }
            std::ifstream inFile("data/"+headerFileName);
            if(inFile.is_open()){
                std::cout << "What part are you looking for?" << std::endl;
                //Used to prevent getline from getting white space
                std::cin.ignore(); 
                getline(std::cin, partName);
                for(int i=0;i<partName.size();i++){
                    partName[i]=std::tolower(partName[i]);
                }
                //Converts the part to lowercase to match with regex
                getline(inFile, firstLine);
                //Determines which header type is the file
                if(firstLine.find("Received")!=std::string::npos){
                    inFile.close();
                    outlook.matchToPart(headerFileName, partName);
                }
                else if(firstLine.find("Delivered-To")!=std::string::npos){
                    inFile.close();
                    gmail.matchToPart(headerFileName, partName);
                }
                else{
                    inFile.close();
                    std::cout << "No proper file found" << std::endl;
                    std::cin.clear();
                }
            }
            else{
                std::cout << "No header file has that name" << std::endl;
                std::cin.clear();
                continue;
            }
        }
        catch(...){
            std::cout << "A file error has occured, please try again." << std::endl;
            std::cin.clear();
        }
    }


    return 0;
}