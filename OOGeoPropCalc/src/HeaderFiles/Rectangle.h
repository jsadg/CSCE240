#include "Shape.h"
#ifndef Rectangle_H

#define Rectangle_H
//Rectangle inherits shape
class Rectangle : public Shape{
    public:
        double length;
        double width;
        Rectangle(double length, double radius);
        //Rectangle constructor and methods
        double calculateArea();
        double calculatePerimeter();

};
#endif