#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

void calculateAreas();
void calculatePerimeters();
std::ifstream inFile("../data/input.txt");
std::ofstream outFile("../data/output.txt");

int main(){
    try{
        //Gets the user's input to see if they want the area of perimeter
        int choice{};
        std::cout << "Enter in 1 for area and 2 for perimeter" << std::endl;
        std::cin >> choice;
        if(choice == 1){
            calculateAreas();
        }
        else if(choice == 2){
            calculatePerimeters();
        }
        else{
            outFile << "No valid option selected";
        }
        inFile.close();
        outFile.close();
        return 0;
    }
    catch(...){
        outFile << "Programmed errored, something was done wrong";
    }

}

    void calculatePerimeters(){
        //First sees if the file exists
        if(inFile.is_open()){
            std::string line;
            std::string type;
            double num1{};
            double num2{};
            double num3{};
            while(getline(inFile, line)){
                //Identifies the type of shape by spliiting at the first space and then makes line the rest of the string past the space
                type=line.substr(0,line.find(" "));
                line=line.substr(line.find(" ")+1);
                if(type==("RECTANGLE")){
                    //Splits the string at the second space and gets the two numbers for length and width
                    //Handles some exceptions by checking to see if the space exists
                    if(line.find(" ")!=std::string::npos){
                        num1=stod(line.substr(0,line.find(" ")));
                        num2=stod(line.substr(line.find(" ")+1));
                        outFile << "RECTANGLE PERIMETER: " + std::to_string((2*num1)+(2*num2)) << std::endl;
                    }
                    else{
                        outFile << "RECTANGLE PERIMETER: Not enough information to calculate" << std::endl;
                    }
                }
                else if(type==("CIRCLE")){
                    //Checks to see if no other space than the inital exists then gets the circle's data
                    if(line.find(" ")==std::string::npos){
                        num1=stod(line);
                        outFile << "CIRCLE PERIMETER: " + std::to_string(2*num1*3.14159) << std::endl;
                    }
                    else{
                        outFile << "CIRCLE PERIMETER: Not enough information to calculate" << std::endl;
                    }
                }
                else if(type==("TRIANGLE")){
                    //Checks if there is another space and then gets the first number before the second space
                    if(line.find(" ")!=std::string::npos){
                        num1=stod(line.substr(0,line.find(" ")));
                        //Moves line to pass the number
                        line=line.substr(line.find(" ")+1);
                    }
                    else{
                        outFile << "TRIANGLE PERIMETER: Not enough information to calculate" << std::endl;
                        continue;
                    }
                    //Checks to see if another space is present and then gets the rest of the data
                    if(line.find(" ")!=std::string::npos){
                        num2=stod(line.substr(0,line.find(" ")));
                        num3=stod(line.substr(line.find(" ")+1));
                        outFile << "TRIANGLE PERIMETER: " + std::to_string(num1+num2+num3) << std::endl;
                    }
                    else{
                        outFile << "TRIANGLE PERIMETER: Not enough information to calculate" << std::endl;
                    }
                }
                else{
                    outFile << "No correct shape input detected" << std::endl;
                }
            }
        }
        else{
            outFile << "No input filed detected";
        }
    }

    void calculateAreas(){
        //First sees if the file exists
        if(inFile.is_open()){
            std::string line;
            std::string type;
            double num1{};
            double num2{};
            double num3{};
            while(getline(inFile, line)){
                //Identifies the type of shape by spliiting at the first space and then makes line the rest of the string past the space
                type=line.substr(0,line.find(" "));
                line=line.substr(line.find(" ")+1);
                if(type==("RECTANGLE")){
                    //Splits the string at the second space and gets the two numbers for length and width
                    //Handles some exceptions by checking to see if the space exists
                    if(line.find(" ")!=std::string::npos){
                        num1=stod(line.substr(0,line.find(" ")));
                        num2=stod(line.substr(line.find(" ")+1));
                        outFile << "RECTANGLE AREA: " + std::to_string(num1*num2) << std::endl;
                    }
                    else{
                        outFile << "RECTANGLE AREA: Not enough information to calculate" << std::endl;
                    }
                }
                else if(type==("CIRCLE")){
                    //Checks to see if no other space than the inital exists then gets the circle's data
                    if(line.find(" ")==std::string::npos){
                        num1=stod(line);
                        outFile << "CIRCLE AREA: " + std::to_string(num1*num1*3.14159) << std::endl;
                    }
                    else{
                        outFile << "CIRCLE AREA: Not enough information to calculate" << std::endl;
                    }
                }
                else if(type==("TRIANGLE")){
                    //Checks if there is another space and then gets the first number before the second space
                    if(line.find(" ")!=std::string::npos){
                        num1=stod(line.substr(0,line.find(" ")));
                        line=line.substr(line.find(" ")+1);
                    }
                    else{
                        outFile << "TRIANGLE AREA: Not enough information to calculate" << std::endl;
                        continue;
                    }
                    //Checks to see if another space is present and then gets the rest of the data
                    if(line.find(" ")!=std::string::npos){
                        num2=stod(line.substr(0,line.find(" ")));
                        num3=stod(line.substr(line.find(" ")+1));
                        double s = (num1+num2+num3)/2.0;
                        outFile << "TRIANGLE AREA: " + std::to_string(sqrt(s*(s-num1)*(s-num2)*(s-num3))) << std::endl;
                    }
                    else{
                        outFile << "TRIANGLE AREA: Not enough information to calculate" << std::endl;
                    }
                }
                else{
                    outFile << "No correct shape input detected" << std::endl;
                }
            }
        }
        else{
            outFile << "No input filed detected";
        }
    }