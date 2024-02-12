#include <iostream>
#include <fstream>


int main(){
    std::string in_file_name = "input.txt";
	std::string out_file_name = "output.txt";
	std::string operation;
    std::string placeholder;
    int x{};
    int y{};
    std::ifstream inFile(in_file_name);
	std::ofstream outFile(out_file_name);
    	if (inFile.is_open()) {
            getline(inFile, operation);
            getline(inFile,placeholder);
            x = stoi(placeholder);
            getline(inFile,placeholder);
            y = stoi(placeholder);
            inFile.close();
            outFile << "The result of "+operation+" on "+std::to_string(x)+" and "+std::to_string(y)+" is below" << std::endl;
            if(operation == ("add")){
                outFile << x+y;
            }
            else if(operation == ("subtract")){
                outFile << x-y;                
            }
            else if(operation == ("multiply")){
                outFile << x*y;                
            }
            else if(operation == ("divide")){
                outFile << (1.0*x)/y;                
            }
            outFile.close();

        }
        else{
            outFile << "No input file detected";
            outFile.close();
        }



}