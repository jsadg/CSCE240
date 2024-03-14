#include <iostream>
#include <regex>
#include <fstream>

#ifndef EMAIL_INFORMATION_EXTRACTOR_H_
#define EMAIL_INFORMATION_EXTRACTOR_H_
class EmailInformationExtractor{
  public:
    std::string received;
    std::string contentType;
    std::string contentTransferEncoding;
    std::string from;
    std::string to;
    std::string CC;
    std::string subject;
    std::string date;
    std::string messageID;
    std::string replyTo;

    //Retrieves information from the file based on the user input
    void getInformation(std::string textName, std::string userInput);
    //Uses Regex to find matching input
    void matchToPart(std::string text,std::string partInput);

};

#endif
