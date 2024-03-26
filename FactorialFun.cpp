#include <iostream>
#include <chrono>

long long computeFactorial(long long num);
long long computeCombination(long long num, long long r);
void printResult(long long num);


int main(){
    bool over = false;
    while(!over){
        try{
            std::string input="";
            std::cout << "Type one number to compute a factorial" << std::endl;
            std::cout << "Two numbers separated by a space to compute a combination" << std::endl;
            std::cout << "Two numbers separated by a space followed by 'compare' to compare the factorial and combination" << std::endl;
            std::cout << "Or q to quit" << std::endl;
            getline(std::cin, input); 
            if(input=="q"){
                over = true;
                break;
            }
            else if(input.find("compare")!=std::string::npos){
                long long firstNum = std::stol(input.substr(0,input.find(" ")));
                input = input.substr(input.find(" ")+1);
                long long secondNum = std::stol(input.substr(0,input.find(" ")));
                auto start = std::chrono::steady_clock::now();
                printResult(computeFactorial(firstNum));
                auto end = std::chrono::steady_clock::now();
                auto elapsed_time = end - start;
    	        std::chrono::duration<double> firstTime = end - start;
                std::cout << "Time for factorial: " << firstTime.count() << std::endl;
                start = std::chrono::steady_clock::now();
                printResult(computeCombination(firstNum, secondNum));
                end = std::chrono::steady_clock::now();
                elapsed_time = end - start;
    	        std::chrono::duration<double> secondTime = end - start;
                std::cout << "Time for combination: " << secondTime.count() << std::endl;
                if(secondTime>firstTime){
                    std::cout << "Time for processing the combination is greater" << std::endl; 
                }
                else{
                    std::cout << "Time for processing the factorial is greater" << std::endl; 
                }
            }
            else if(input.find(" ")!=std::string::npos){
                long long firstNum = std::stol(input.substr(0,input.find(" ")));
                long long secondNum = std::stol(input.substr(input.find(" ")+1));
                auto start = std::chrono::steady_clock::now();
                printResult(computeCombination(firstNum, secondNum));
                auto end = std::chrono::steady_clock::now();
                auto elapsed_time = end - start;
    	        std::chrono::duration<double> DiffInSeconds = end - start;
                std::cout << "Time for processing: " << DiffInSeconds.count() << std::endl;
            }      
            else{
                long long firstNum = std::stol(input);
                auto start = std::chrono::steady_clock::now();
                printResult(computeFactorial(firstNum));             
                auto end = std::chrono::steady_clock::now();
                auto elapsed_time = end - start;
    	        std::chrono::duration<double> DiffInSeconds = end - start;
                std::cout << "Time for processing: " << DiffInSeconds.count() << std::endl;
            }  
        }
        catch(...){
            std::cout << "There was an error in your input, please try again" << std::endl;
        }
    }

    return 0;
}



long long computeFactorial(long long num) { 
    if(num == 0 || num == 1){ 
        return 1;  
    } 
    else{ 
        return num*computeFactorial(num-1);
    } 
} 

long long computeCombination(long long num, long long r) { 
    if(r>num){
        return 0;
    }
    return computeFactorial(num)/(computeFactorial(r)*computeFactorial(num-r));
} 


void printResult(long long num){
    if(num == 0 || num<0){
        std::cout << "Your number is either too large or invalid" << std::endl;
    }
    else{
        std::cout << "Your result is: " << num << std::endl;
    }
}