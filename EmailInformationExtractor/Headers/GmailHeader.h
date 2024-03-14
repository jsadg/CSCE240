#include <iostream>
#include <regex>
#include "EmailInformationExtractor.h"

#ifndef GMAIL_HEADER_H_
#define GMAIL_HEADER_H_

class GmailHeader : public EmailInformationExtractor{
    public:
        std::string deliveredTo;
        std::string xGoogleSmtpSource;
        std::string mimeVerison;
        GmailHeader();

        //Uses Regex to find matching input
        void matchToPart(std::string text,std::string partInput);


};

#endif