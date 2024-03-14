#include <iostream>
#include <fstream>
#include <regex>
#include "EmailInformationExtractor.h"

#ifndef OUTLOOK_HEADER_H_
#define OUTLOOK_HEADER_H_

class OutlookHeader : public EmailInformationExtractor{
    public:
        OutlookHeader();

        std::string authenticationResults;
        std::string threadTopic;
        std::string threadIndex;
        std::string references;
        std::string acceptLanguage;
        std::string contentLanguage;
        std::string xmsHasAttach;
        std::string xmsExchangeOrganizationSCL;

        //Uses Regex to find matching input
        void matchToPart(std::string text,std::string partInput);


};

#endif
