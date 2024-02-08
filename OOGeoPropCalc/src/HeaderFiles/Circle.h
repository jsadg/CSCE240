#include "Shape.h"
#ifndef Circle_H

#define Circle_H
//Circle inherits shape
class Circle : public Shape{
    public:
        double radius;
        Circle(double radius);
        //Circle constructor and methods
        double calculateArea();
        double calculatePerimeter();
};
#endif