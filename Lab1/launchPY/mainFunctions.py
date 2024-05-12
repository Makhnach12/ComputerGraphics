import ctypes

from Lab2.dot import Dot

task = ctypes.CDLL('tasks.so')
line = ctypes.CDLL('line.so')
ctypes.cdll.LoadLibrary('operations.so')
ctypes.cdll.LoadLibrary('dotOperations.so')


def relation2Line(coef1: tuple[float, ...], coef2: tuple[float, ...]) -> int:
    line.newLine.restype = ctypes.c_void_p
    line.newLine.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
    line1 = line.newLine(coef1[0], coef1[1], coef1[2])
    line2 = line.newLine(coef2[0], coef2[1], coef2[2])
    task.relation2Line.restype = ctypes.c_int
    task.relation2Line.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    return task.relation2Line(line1, line2)


def isRayIntersectSegment(dotA: tuple[float, ...], dotB: tuple[float, ...],
                          dotC: tuple[float, ...], dotD: tuple[float, ...]) \
        -> bool:
    line.newDot2D.restype = ctypes.c_void_p
    line.newDot2D.argtypes = [ctypes.c_double, ctypes.c_double]

    dotA = line.newDot2D(dotA[0], dotA[1])
    dotB = line.newDot2D(dotB[0], dotB[1])
    dotC = line.newDot2D(dotC[0], dotC[1])
    dotD = line.newDot2D(dotD[0], dotD[1])

    task.isRayIntersectSegment.restype = ctypes.c_bool
    task.isRayIntersectSegment.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                           ctypes.c_void_p, ctypes.c_void_p]
    return task.isRayIntersectSegment(dotA, dotB, dotC, dotD)


def analyzeAngle(dotA: tuple[float, ...], dotB: tuple[float, ...],
                 dotC: tuple[float, ...]) -> int:
    line.newDot3D.restype = ctypes.c_void_p
    line.newDot3D.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]

    dotA = line.newDot3D(dotA[0], dotA[1], dotA[2])
    dotB = line.newDot3D(dotB[0], dotB[1], dotB[2])
    dotC = line.newDot3D(dotC[0], dotC[1], dotC[2])

    task.analyzeAngle.restype = ctypes.c_int
    task.analyzeAngle.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                  ctypes.c_void_p]
    return task.analyzeAngle(dotA, dotB, dotC)


def analyzeDots(dotA: tuple[float, ...], dotB: tuple[float, ...],
                dotC: tuple[float, ...]) -> bool:
    line.newDot3D.restype = ctypes.c_void_p
    line.newDot3D.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]

    dotA = line.newDot3D(dotA[0], dotA[1], dotA[2])
    dotB = line.newDot3D(dotB[0], dotB[1], dotB[2])
    dotC = line.newDot3D(dotC[0], dotC[1], dotC[2])

    task.analyzeDots.restype = ctypes.c_bool
    task.analyzeDots.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                 ctypes.c_void_p]
    return task.analyzeDots(dotA, dotB, dotC)


def analyzeTriangle(dotA: tuple[float, ...], dotB: tuple[float, ...],
                    dotC: tuple[float, ...]) -> list[float]:
    line.newDot3D.restype = ctypes.c_void_p
    line.newDot3D.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]

    dotA = line.newDot3D(dotA[0], dotA[1], dotA[2])
    dotB = line.newDot3D(dotB[0], dotB[1], dotB[2])
    dotC = line.newDot3D(dotC[0], dotC[1], dotC[2])

    task.analyzeTriangle.restype = ctypes.POINTER(ctypes.c_double * 3)
    task.analyzeTriangle.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                     ctypes.c_void_p]

    resultPtr = task.analyzeTriangle(dotA, dotB, dotC)
    result = [round(value, 5) for value in resultPtr.contents]
    return result


def getAngle(dotA: Dot, dotB: Dot, dotC: Dot) -> float:
    line.newDot3D.restype = ctypes.c_void_p
    line.newDot3D.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]

    dotA = line.newDot3D(dotA.x, dotA.y, 0)
    dotB = line.newDot3D(dotB.x, dotB.y, 0)
    dotC = line.newDot3D(dotC.x, dotC.y, 0)

    task.getAngle.restype = ctypes.c_double
    task.getAngle.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                              ctypes.c_void_p]

    return task.getAngle(dotA, dotB, dotC)