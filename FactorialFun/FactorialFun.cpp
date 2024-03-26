#include <iostream>
#include <chrono>

//Methods
long long computeFactorial(long long num);
long long computeCombination(long long num, long long r);
void printResult(long long num);


int main(){
    bool over = false;
    //Loops continuously until the user wants to stop
    while(!over){
        try{
            std::string input="";
            std::cout << "Type one number to compute a factorial" << std::endl;
            std::cout << "Two numbers separated by a space to compute a combination" << std::endl;
            std::cout << "Two numbers separated by a space followed by 'compare' to compare the factorial and combination" << std::endl;
            std::cout << "Or q to quit" << std::endl;
            getline(std::cin, input); 
            //If the user types 'q' then the program quits
            if(input=="q"){
                over = true;
                break;
            }
            //If the user includes the word compare then the program looks for the values seperated by a space
            else if(input.find("compare")!=std::string::npos){
                //Values are retrieved
                long long firstNum = std::stol(input.substr(0,input.find(" ")));
                input = input.substr(input.find(" ")+1);
                long long secondNum = std::stol(input.substr(0,input.find(" ")));
                //Timer is started and stopped for the factorial time
                auto start = std::chrono::steady_clock::now();
                printResult(computeFactorial(firstNum));
                auto end = std::chrono::steady_clock::now();
                auto elapsed_time = end - start;
    	        std::chrono::duration<double> firstTime = end - start;
                std::cout << "Time for factorial: " << firstTime.count() << std::endl;
                //Time is started and stopped for the combination time
                start = std::chrono::steady_clock::now();
                printResult(computeCombination(firstNum, secondNum));
                end = std::chrono::steady_clock::now();
                elapsed_time = end - start;
    	        std::chrono::duration<double> secondTime = end - start;
                std::cout << "Time for combination: " << secondTime.count() << std::endl;
                //The factorial and combination time are compared and the greater one is printed out
                if(secondTime>firstTime){
                    std::cout << "Time for processing the combination is greater" << std::endl; 
                }
                else{
                    std::cout << "Time for processing the factorial is greater" << std::endl; 
                }
            }
            //If the word compare was not included then the program checks to see if it's a combination
            else if(input.find(" ")!=std::string::npos){
                //Inputs for a combination are looked for
                long long firstNum = std::stol(input.substr(0,input.find(" ")));
                long long secondNum = std::stol(input.substr(input.find(" ")+1));
                //Timer is started and stopped for a combination
                auto start = std::chrono::steady_clock::now();
                printResult(computeCombination(firstNum, secondNum));
                auto end = std::chrono::steady_clock::now();
                auto elapsed_time = end - start;
    	        std::chrono::duration<double> DiffInSeconds = end - start;
                //Time is printed out
                std::cout << "Time for processing: " << DiffInSeconds.count() << std::endl;
            }      
            else{
                //Otherwise assume its a factorial
                long long firstNum = std::stol(input);
                //Timer starts and stops for the factorial
                auto start = std::chrono::steady_clock::now();
                printResult(computeFactorial(firstNum));             
                auto end = std::chrono::steady_clock::now();
                auto elapsed_time = end - start;
    	        std::chrono::duration<double> DiffInSeconds = end - start;
                //Time is printed out
                std::cout << "Time for processing: " << DiffInSeconds.count() << std::endl;
            }  
        }
        //This catches other user inputs such as decimals or strings as they would cause errors
        catch(...){
            std::cout << "There was an error in your input, please try again" << std::endl;
        }
    }

    return 0;
}



long long computeFactorial(long long num) { 
    //Avoids errors with negative numbers
    if(num < 0){
        return 0;
    }
    //Stopping condition for recursion
    if(num == 0 || num == 1){ 
        return 1;  
    } 
    else{ 
        return num*computeFactorial(num-1);
    } 
} 

long long computeCombination(long long num, long long r) { 
    //Avoids any input of bad numbers to factorial
    if(num < 0 || r < 0){
        return 0;
    }
    //Avoids r > 0 bad case
    if(r>num){
        return 0;
    }
    //Avoids division by 0
    if(computeFactorial(r)*computeFactorial(num-r) == 0){
        return 0;
    }
    return computeFactorial(num)/(computeFactorial(r)*computeFactorial(num-r));
} 


void printResult(long long num){
    //If the number is less or equal to 0 that means somewhere in the program the output is an overflow or wrong
    if(num == 0 || num < 0){
        std::cout << "Your number is either too large or invalid" << std::endl;
    }
    else{
        std::cout << "Your result is: " << num << std::endl;
    }
}