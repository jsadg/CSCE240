#include "Shape.h"
#include <cmath>
#ifndef Triangle_H

#define Triangle_H
//Triangle inherits shape
class Triangle : public Shape{
    public:
        double side1;
        double side2;
        double side3;
        Triangle(double side1, double side2, double side3);
        //Constructor and methods for triangles
        double calculateArea();
        double calculatePerimeter();
};
#endif