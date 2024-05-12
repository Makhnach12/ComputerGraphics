#include "Tasks.hpp"

int relation2Line(Line2D *lin1, Line2D *lin2) {
    return lin1->relation2Line(*lin2);
}

bool isRayIntersectSegment(Dot2D* dotA, Dot2D* dotB, Dot2D* dotC, Dot2D* dotD){
    Line2D lin1(*dotA, *dotB);
    Line2D lin2(*dotC, *dotD);
    Dot2D res(1, 1);
    if (((dotC->getX() >= dotA->getX()) == (dotB->getX() >= dotA->getX())
        && (dotC->getY() >= dotA->getY()) == (dotB->getY() >= dotA->getY())) ||
        ((dotD->getX() >= dotA->getX()) == (dotB->getX() >= dotA->getX())
         && (dotD->getY() >= dotA->getY()) == (dotB->getY() >= dotA->getY()))){
        return true;
    }
    return false;
}

int analyzeAngle(Dot3D* dot1, Dot3D* dot2, Dot3D* dot3){
    double angle = unfoldedAngle / PI * findAngle3D(*dot1, *dot2, *dot3);
    if (angle < straightAngle){
        return 1;
    }
    else if (abs(angle - straightAngle) < EPS){
        return 2;
    }
    else{
        return 3;
    }
}

bool analyzeDots(Dot3D* dot1, Dot3D* dot2, Dot3D* dot3){
    double angle = unfoldedAngle / PI * findAngle3D(*dot1, *dot2, *dot3);
    if (abs(angle -  unfoldedAngle) < EPS or angle < EPS){
        return true;
    }
    return false;
}

double getAngle(Dot3D* dot1, Dot3D* dot2, Dot3D* dot3){
    return unfoldedAngle / PI * findAngle3D(*dot1, *dot2, *dot3);
}

double* analyzeTriangle(Dot3D* A, Dot3D* B, Dot3D* C){
    double* arrAns = new double[3];
    arrAns[0] = giveHeight(distance3D(*A, *B), distance3D(*A, *C), distance3D(*B, *C));
    arrAns[1] = giveMedian(*A, *B, *C);
    arrAns[2] = giveBisector(*A, *B, *C);
    return arrAns;
}

