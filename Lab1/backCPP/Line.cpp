#include "Line.hpp"
double getX(Dot2D *dot){ return dot->getX();}
double getY(Dot2D *dot){ return dot->getY();}

Dot2D *newDot2D(double x, double y) {
    return new Dot2D(x,y);
}

void delDot(Dot2D *dot) {
    delete dot;
}

double getA(Line2D *lin){ return lin->getA();}
double getB(Line2D *lin){ return lin->getB();}
double getC(Line2D *lin){ return lin->getC();}

int Line2D::relation2Line(Line2D lin) {
    if (_a == lin._a and _b == lin._b and _c == lin._c){
//        return "Equal";
        return 1;
    }
    else if (_a == lin._a and _b == lin._b){
//        return "Parallel";
        return 2;
    }
    else{
//        return "Don't overlap";
        return 3;
    }
}

//Одним из способов решения системы является метод Крамера. Для его применения необходимо определить определители матрицы системы:
//
//Определитель главной матрицы: D = ae — bd
//Определитель матрицы X: Dx = c1e — c2b
//Определитель матрицы Y: Dy = ac2 — c1d
//После нахождения определителей, можно найти координаты точки пересечения прямых:
//
//x = Dx / D
//y = Dy / D
//Таким образом, используя формулу для нахождения координат точки пересечения, можно определить точку, в которой две прямые пересекаются.

bool Line2D::findPointIntersec(Line2D lin, Dot2D& dot) {
    double mainDet = determinant(_a, _b, lin._a, lin._b);
    if (abs(mainDet) < EPS){
        if (abs(determinant(_a, _c, lin._a, lin._c)) != 0
            or abs(determinant(_b, _c, lin._b, lin._c)) != 0){
            return false;
        }
    }
    dot._x = -determinant(_c, _b, lin._c, lin._b) / mainDet;
    dot._y = -determinant(_a, _c, lin._a, lin._c) / mainDet;
    return true;
}

Line2D *newLine(double a, double b, double c) {
    return new Line2D(a, b, c);
}

void delLine(Line2D *lin) {
    delete lin;
}

Dot3D *newDot3D(double x, double y, double z){
    return new Dot3D(x, y, z);
}
