#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include "Circle.cpp"
#include "Rectangle.cpp"
#include "Triangle.cpp"

void calculate();
std::ifstream inFile("../data/input.txt");
std::ofstream outFile("../data/output.txt");
//aorp represents area or perimeter
std::string aorp = "";

int main(){
    try{
        //Gets the user's input to see if they want the area of perimeter
        int choice{};
        std::cout << "Enter in 1 for area and 2 for perimeter" << std::endl;
        std::cin >> choice;
        if(choice == 1){
            //Option1 sets aorp to area
            aorp = "AREA";
            calculate();
        }
        else if(choice == 2){
            //Option2 sets aorp to perimeter
            aorp = "PERIMETER";
            calculate();
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
    void calculate(){
        //First sees if the file exists
        if(inFile.is_open()){
            std::string line;
            std::string type;
            double num1{};
            double num2{};
            double num3{};
            while(getline(inFile, line)){
                try{
                    //Identifies the type of shape by spliiting at the first space and then makes line the rest of the string past the space
                    type=line.substr(0,line.find(" "));
                    line=line.substr(line.find(" ")+1);
                    if(type==("RECTANGLE")){
                        //Splits the string at the second space and gets the two numbers for length and width
                        //Handles some exceptions by checking to see if the space exists
                        if(line.find(" ")!=std::string::npos){
                            num1=stod(line.substr(0,line.find(" ")));
                            num2=stod(line.substr(line.find(" ")+1));
                            //Creates a rectangle object with the numbers
                            Rectangle rec(num1,num2);
                            //Checks to see if the values are reasonable
                            if(num1>0 && num2>0){
                                //Based on aorp prints perimeter or area information
                                if(aorp=="PERIMETER"){
                                    outFile << "RECTANGLE PERIMETER: " + std::to_string(rec.calculatePerimeter()) << std::endl;                    
                                }
                                else{
                                    outFile << "RECTANGLE AREA: " + std::to_string(rec.calculateArea()) << std::endl;                    
                                }
                            }
                            else{
                                outFile << "RECTANGLE " << aorp << ": Negative or 0"  << std::endl;
                            }
                        }
                        else{
                            outFile << "RECTANGLE " << aorp << ": Not enough information to calculate" << std::endl;
                        }
                    }
                    else if(type==("CIRCLE")){
                        //Checks to see if no other space than the inital exists then gets the circle's data
                        if(line.find(" ")==std::string::npos){
                            num1=stod(line);
                            //Creates a shape object with the number
                            Circle cir(num1);
                            //Checks to see if the radius is reasonable
                            if(num1>0){
                                //Prints area or perimeter information based on aorp 
                                if(aorp=="PERIMETER"){
                                    outFile << "CIRCLE PERIMETER: " + std::to_string(cir.calculatePerimeter()) << std::endl;                    
                                }
                                else{
                                    outFile << "CIRCLE AREA: " + std::to_string(cir.calculateArea()) << std::endl;                    
                                }
                            }
                            else{
                                outFile << "CIRCLE " << aorp << ": Negative or 0"  << std::endl;
                            }
                        }
                        else{
                            outFile << "CIRCLE " << aorp << ": Not enough information to calculate" << std::endl;
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
                            //Creates a triangle object with the three nums
                            Triangle tri(num1,num2,num3);
                            //Checks to see if the nums are reasonable
                            if(num1>0 && num2>0 && num3>0){
                                //Based on aorp prints triangle or perimeter information
                                if(aorp=="PERIMETER"){
                                    outFile << "TRIANGLE PERIMETER: " + std::to_string(tri.calculatePerimeter()) << std::endl;                    
                                }
                                else{
                                    outFile << "TRIANGLE AREA: " + std::to_string(tri.calculateArea()) << std::endl;                    
                                }
                            }
                            else{
                                outFile << "TRIANGLE " << aorp << ": Negative or 0"  << std::endl;
                            }
                        }
                        else{
                            outFile << "TRIANGLE PERIMETER: Not enough information to calculate" << std::endl;
                        }
                    }
                    else{
                        outFile << "No correct shape input detected" << std::endl;
                    }
                }
                catch(...){
                    outFile << "Invalid shape information" << std::endl;
                }
            }
        }
        else{
            outFile << "No input filed detected";
        }
    }