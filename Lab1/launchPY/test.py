import unittest

from Lab1.launchPY.mainFunctions import relation2Line, isRayIntersectSegment, \
    analyzeAngle, analyzeDots, analyzeTriangle


class TestLab1(unittest.TestCase):
    def testRelation2Line1(self):
        self.assertEqual(relation2Line((1, 1, 1), (1, 1, 1)), 1)

    def testRelation2Line2(self):
        self.assertEqual(relation2Line((1, 2, 4), (1, 2, 3)), 2)

    def testRelation2Line3(self):
        self.assertEqual(relation2Line((4, 4, 4), (1, 2, 3)), 3)

    def testIsRayIntersectSegment1(self):
        self.assertEqual(isRayIntersectSegment((0, 0), (1, 0), (-2, 0),
                                               (-1, 0)), False)

    def testIsRayIntersectSegment2(self):
        self.assertEqual(isRayIntersectSegment((0, 0), (1, 1), (-1, -1),
                                               (-2, -2)), False)

    def testIsRayIntersectSegment3(self):
        self.assertEqual(isRayIntersectSegment((0, 0), (1, 0), (-1, 0),
                                               (0, 0)), True)

    def testIsRayIntersectSegment4(self):
        self.assertEqual(isRayIntersectSegment((0, 0), (1, 0), (-1, 0),
                                               (0.5, 0)), True)

    def testIsRayIntersectSegment5(self):
        self.assertEqual(isRayIntersectSegment((0, 0), (1, 0), (100, 0),
                                               (101, 0)), True)

    def testAnalyzeAngle1(self):
        self.assertEqual(analyzeAngle((0, 1, 0), (0, 0, 0), (1, 0, 0)), 2)

    def testAnalyzeAngle2(self):
        self.assertEqual(analyzeAngle((-1, 0, 0), (0, 0, 0), (1, 0, 0)), 3)

    def testAnalyzeAngle3(self):
        self.assertEqual(analyzeAngle((0.5, 0.5, 0), (0, 0, 0), (0.5, 0, 0)), 1)

    def testAnalyzeAngle4(self):
        self.assertEqual(analyzeAngle((1, 1, 1), (0, 0, 0), (-1, 1, 1)), 1)

    def testAnalyzeDots1(self):
        self.assertEqual(analyzeDots((0, 0, 0), (1, 1, 1), (2, 2, 2)), True)

    def testAnalyzeDots2(self):
        self.assertEqual(analyzeDots((0, 0, 0), (1, 1, 1), (2, 2, 0)), False)

    def testAnalyzeTriangle1(self):
        self.assertEqual(analyzeTriangle((0, 0, 0), (1, 0, 0), (0, 1, 0)),
                         [0.70711, 0.70711, 0.70721])

    def testAnalyzeTriangle2(self):
        self.assertEqual(analyzeTriangle((0, 0, 0), (1, 1, 0), (-1, 1, 0)),
                         [1.0, 1.0, 1.00015])

    def testAnalyzeTriangle3(self):
        self.assertEqual(analyzeTriangle((0, -1, 0), (-1, 1, 0), (-2, 1, 0)),
                         [2.0, 2.5, 2.46635])


if __name__ == "__main__":
    unittest.main()
