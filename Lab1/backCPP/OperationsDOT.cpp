#include "OperationsDOT.hpp"
#include "Operations.hpp"

double sсalar3D(Dot3D& dot1, Dot3D& dot2){
    return dot1.getX() * dot2.getX() + dot1.getY() * dot2.getY() + dot1.getZ() * dot2.getZ();
}

double vector3DLen(Dot3D& dot){
    return sqrt(dot.getX() * dot.getX() + dot.getY() * dot.getY() +
                dot.getZ() * dot.getZ());
}

double distance3D(Dot3D& dot1, Dot3D& dot2){
    return sqrt(pow((dot1.getX() - dot2.getX()), 2) +
                pow((dot1.getY() - dot2.getY()), 2) +
                pow((dot1.getZ() - dot2.getZ()), 2));
}

double giveHeight(double AB, double AC, double BC){
    double halfPerimeter = (AB + AC + BC) / 2;
    return 2 * sqrt(halfPerimeter * (halfPerimeter - AB) *
                    (halfPerimeter - AC) *
                    (halfPerimeter - BC)) / BC;
}

double giveMedian(Dot3D& A, Dot3D& B, Dot3D& C){
    Dot3D midDotBC((B.getX() + C.getX()) / 2, (B.getY() + C.getY()) / 2,
                   (B.getZ() + C.getZ()) / 2);
    return distance3D(midDotBC, A);
}

double giveBisector(Dot3D& A, Dot3D& B, Dot3D& C){
    double angleACB = findAngle3D(A, C, B);
    double angleBAC = findAngle3D(B, A, C);
    double AC = distance3D(A, C);
    return AC * sin(angleACB) / sin(PI - angleBAC / 2 - angleACB);
}


double findAngle3D(Dot3D& dot1, Dot3D& dot2, Dot3D& dot3) {
    Dot3D dot1_shift(dot1.getX() - dot2.getX(), dot1.getY() - dot2.getY(),
                     dot1.getZ() - dot2.getZ());
    Dot3D dot3_shift(dot3.getX() - dot2.getX(), dot3.getY() - dot2.getY(),
                     dot3.getZ() - dot2.getZ());
    return acos(round(sсalar3D(dot1_shift, dot3_shift) /
                      (vector3DLen(dot1_shift) * vector3DLen(dot3_shift)) * 1000) / 1000);
}
