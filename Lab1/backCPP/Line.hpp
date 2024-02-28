#ifndef Line_hpp
//#pragma once
#include <iostream>
#include <string.h>
#include "Operations.hpp"

class Dot2D{
    friend class Line2D;
private:
    double _x, _y;
public:
    Dot2D(double x, double y){ _x = x; _y = y;}
    double getX(){ return _x;}
    double getY(){ return _y;}
    
    void setX(double x){ _x = x; }
    void setY(double y){ _y = y; }
};


class Line2D{
private:
    double _a, _b, _c;
public:
    Line2D(double a, double b, double c){
        _a = a;
        _b = b;
        _c = c;
    }
    Line2D(Dot2D dot1, Dot2D dot2){
        _a = dot2._y - dot1._y;
        _b = -(dot2._x - dot1._x);
        _c = -dot1._x * (dot2._y - dot1._y) + dot1._y * (dot2._x - dot1._x);
    }
    
    bool findPointIntersec(Line2D lin, Dot2D& dot);
    int relation2Line(Line2D);
    double getA(){ return _a;}
    double getB(){ return _b;}
    double getC(){ return _c;}
};

class Dot3D: public Dot2D
{
private:
    double _z;
public:
    Dot3D(double x, double y, double z): Dot2D(x, y){
        _z = z;
    }
    double getZ(){ return _z;}
    
    void setZ(double z){ _z = z; }
};

class Line3D
{
private:
    double _a, _b, _c, _d;
public:
    Line3D(double a, double b, double c, double d){
        _a = a;
        _b = b;
        _c = c;
        _d = d;
    }
    
    double getA(){ return _a;}
    double getB(){ return _b;}
    double getC(){ return _c;}
    double getD(){ return _d;}
};

#ifdef __cplusplus
extern "C" {
#endif
    Dot2D *newDot2D(double x, double y);
    void delDot(Dot2D *dot);
    double getX(Dot2D *dot);
    double getY(Dot2D *dot);

    Dot3D *newDot3D(double x, double y, double z);

    Line2D *newLine(double a, double b, double c);
    void delLine(Line2D *lin);
    double getA(Line2D *lin);
    double getB(Line2D *lin);
    double getC(Line2D *lin);
#ifdef __cplusplus
}
#endif
#endif /* Line2D_hpp */
