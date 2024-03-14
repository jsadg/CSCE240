#include "Headers/GmailHeader.h"
//Constructor definition
GmailHeader::GmailHeader() {
    EmailInformationExtractor();
}

//MatchToPart Definition
void GmailHeader::matchToPart(std::string text,std::string partInput) {
    if(std::regex_match(partInput, std::regex(".*delive(red)?[ -]?to"))){
        EmailInformationExtractor::getInformation(text, "Delivered-To");
    }
    else if(std::regex_match(partInput, std::regex(".*x[ -]?googl(e)?[ -]?smt(p)?"))){
        EmailInformationExtractor::getInformation(text, "X-Google-Smtp-Source");
    }
    else if(std::regex_match(partInput, std::regex(".*mim(e)?[ -]?vers"))){
        EmailInformationExtractor::getInformation(text, "Mime-Version");
    }
    //If no option is found specifically for outlook then looks for shared attributes
    else{
        EmailInformationExtractor::matchToPart(text, partInput);       
    }
        
}