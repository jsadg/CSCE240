#include "HeaderFiles/Shape.h"
#include "HeaderFiles/Triangle.h"

//Triangle class constructor
Triangle::Triangle(double side1, double side2, double side3){
    this->side1 = side1;
    this->side2 = side2;
    this->side3 = side3;
}

double Triangle::calculateArea(){
    //Calculates area
    double s = (side1+side2+side3)/2;
    return sqrt(s*(s-side1)*(s-side2)*(s-side3));
}

double Triangle::calculatePerimeter(){
    //Calculates perimeter
    return side1+side2+side3;
}