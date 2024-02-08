#include "HeaderFiles/Shape.h"
#include "HeaderFiles/Rectangle.h"

//Rectangle class constructor
Rectangle::Rectangle(double length, double width){
    this->length = length;
    this->width = width;

}

double Rectangle::calculateArea(){
    //Calculates area
    return length*width;
}

double Rectangle::calculatePerimeter(){
    //Calculates perimeter
    return 2*(length+width);
}