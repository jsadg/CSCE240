#include "Headers/OutlookHeader.h"

//Constructor Definition
OutlookHeader::OutlookHeader() {
    EmailInformationExtractor();
}

//MatchToPart Definition
void OutlookHeader::matchToPart(std::string text,std::string partInput) {
    if(std::regex_match(partInput, std::regex(".*auth(entication)?[ -]?resu.*"))){
        EmailInformationExtractor::getInformation(text, "Authentication-Results");
    }
    else if(std::regex_match(partInput, std::regex(".*hread[ -]?topi.*"))){
        EmailInformationExtractor::getInformation(text, "Thread-Topic");
    }
    else if(std::regex_match(partInput, std::regex(".*hread[ -]?ind.*"))){
        EmailInformationExtractor::getInformation(text, "Thread-Index");
    }
    else if(std::regex_match(partInput, std::regex(".*referenc.*"))){
        EmailInformationExtractor::getInformation(text, "References");
    }
    else if(std::regex_match(partInput, std::regex(".*acce(pt)?[ -]?lang(uage)"))){
        EmailInformationExtractor::getInformation(text, "Accept-Language");
    }
    else if(std::regex_match(partInput, std::regex(".*cont(ent)?[ -]?lang(uage)"))){
        EmailInformationExtractor::getInformation(text, "Content-Language");
    }
    else if(std::regex_match(partInput, std::regex(".*x[ -]?ms[ -]?has[ -]?att"))){
        EmailInformationExtractor::getInformation(text, "X-MS-Has-Attach");
    }
    else if(std::regex_match(partInput, std::regex(".*x[ -]?ms[ -]?excha(nge)?[ -]?org"))){
        EmailInformationExtractor::getInformation(text, "X-MS-Exchange-Organization-SCL");
    }
    //If no option is found specifically for outlook then looks for shared attributes
    else{
        EmailInformationExtractor::matchToPart(text, partInput);       
    }
        
}

