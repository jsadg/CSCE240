#include <string>
#ifndef Shape_H

#define Shape_H
class Shape{
    public:
        //Instance variables for shapes
        double area;
        double perimeter;
        std::string errorMessage;
        //Methods for shapes
        double getArea();
        double getPerimeter();
        std::string getErrorMessage();
};
#endif