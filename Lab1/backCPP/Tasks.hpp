#ifndef Tasks_hpp
#define Tasks_hpp
#define unfoldedAngle 180.0
#define straightAngle 90.0

#include <stdio.h>
#include "OperationsDOT.hpp"


#ifdef __cplusplus
extern "C" {
#endif
    int relation2Line(Line2D* lin1, Line2D* lin2);

    bool isRayIntersectSegment(Dot2D* dotA, Dot2D* dotB, Dot2D* dotC, Dot2D* dotD);

    int analyzeAngle(Dot3D* dot1, Dot3D* dot2, Dot3D* dot3);

    bool analyzeDots(Dot3D* dot1, Dot3D* dot2, Dot3D* dot3);

    double* analyzeTriangle(Dot3D* A, Dot3D* B, Dot3D* C);

    double getAngle(Dot3D* dot1, Dot3D* dot2, Dot3D* dot3);
#ifdef __cplusplus
}
#endif

#endif /* Tasks_hpp */
