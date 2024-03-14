#include "Headers/EmailInformationExtractor.h"

    //Get information definition
    void EmailInformationExtractor::getInformation(std::string textName, std::string userInput){
        std::ifstream inFile("data/"+textName);
        std::string text = "";
        while(getline(inFile, text)){
            if(text.find(userInput+":")!= std::string::npos){
                std::cout << text << std::endl;
            }
        }
    }

    //Match to part definition
    void EmailInformationExtractor::matchToPart(std::string text,std::string partInput) {
        if(std::regex_match(partInput, std::regex(".*receiv.*"))){
            getInformation(text, "Received");
        }
        else if(std::regex_match(partInput, std::regex(".*cont(ent)?[ -]?typ(e)?"))){
            getInformation(text, "Content-Type");
        }
        else if(std::regex_match(partInput, std::regex(".*cont(ent)?[ -]transf(er)?[ -]?encod(ing)?"))){
           getInformation(text, "Content-Transfer-Encoding");
        }
        else if(std::regex_match(partInput, std::regex(".*from$"))){
           getInformation(text, "From");
        }
        else if(std::regex_match(partInput, std::regex("to$"))){
           getInformation(text, "To");
        }
        else if(std::regex_match(partInput, std::regex("cc$"))){
           getInformation(text, "CC");
        }
        else if(std::regex_match(partInput, std::regex(".*subje(ct)?(s)?"))){
           getInformation(text, "Subject");
        }
        else if(std::regex_match(partInput, std::regex(".*date$"))){
           getInformation(text, "Date");
        }
        else if(std::regex_match(partInput, std::regex(".*messag(e)?( -)?id"))){
           getInformation(text, "Message-ID");
        }
        else if(std::regex_match(partInput, std::regex(".*rep(ly)?[ -]?to"))){
           getInformation(text, "Reply-To");
        }
        else{
            std::cout << "No valid part detected, please try again" << std::endl;
        }
    }


 