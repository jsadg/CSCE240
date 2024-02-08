#include "HeaderFiles/Shape.h"
#include "HeaderFiles/Circle.h"

//Circle constructor
Circle::Circle(double radius){
    this->radius = radius;
}

double Circle::calculateArea(){
    //Calculates area
    return 3.141592653589793238462643383279502884197169 * radius * radius;
}

double Circle::calculatePerimeter(){
    //Calculates perimeter
    return 3.141592653589793238462643383279502884197169 * 2 * radius;
}