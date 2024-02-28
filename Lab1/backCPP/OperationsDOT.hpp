#ifndef OperationsDOT_hpp
#define OperationsDOT_hpp

#include <stdio.h>
#include "Line.hpp"
#include <cmath>

double sсalar3D(Dot3D& dot1, Dot3D& dot2);

double vector3DLen(Dot3D& dot);

double distance3D(Dot3D& dot1, Dot3D& dot2);

double giveHeight(double AB, double AC, double BC);

double giveMedian(Dot3D& A, Dot3D& B, Dot3D& C);

double giveBisector(Dot3D& A, Dot3D& B, Dot3D& C);

double findAngle3D(Dot3D& dot1, Dot3D& dot2, Dot3D& dot3);


#endif /* OperationsDOT_hpp */
