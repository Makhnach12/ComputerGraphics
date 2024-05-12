#include <iostream>
#include "Tasks.hpp"

int main(){
//    int a, b, c;
    Dot3D* dotA = newDot3D(0, -1, 0);
    Dot3D* dotB = new Dot3D(-1, 1, 0);
    Dot3D* dotC = new Dot3D(-2, 1, 0);
    
    Dot2D* dotAa = new Dot2D(0.2, 0);
    Dot2D* dotBb = new Dot2D(1, 0);
    Dot2D* dotCc = new Dot2D(0, 0);
    Dot2D* dotDd = new Dot2D(-1, 0);
//    Dot2D* dotD = new Dot2D(1.5, 0);
//    a = 1;
//    b = 2;
//    c = 3;
//    Line* lin1 = newLine(a, b, c);
//    Line* lin2 = newLine(a, -b, c);
//    lin1 -> findPointIntersec(*lin2, dot);
//    std::cout << isRayIntersectSegment(dotA, dotB, dotC, dotD);
    std::cout << getAngle(dotA, dotC, dotB) << '\n';
//    double* arr = analyzeTriangle(dotA, dotB, dotC);
//    std::cout << arr[0] << ' ' << arr[1] << ' ' << arr[2];
    return 0;
}
