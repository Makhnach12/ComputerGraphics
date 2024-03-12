import numpy as np

WIDTH = 600
HEIGHT = 600
MIDDLE = (WIDTH // 2, HEIGHT // 2)

MATRIX_UP = [[1, 0, 0], [0, 1, 0], [0, 1, 1]]
MATRIX_DOWN = [[1, 0, 0], [0, 1, 0], [0, -1, 1]]
MATRIX_RIGHT = [[1, 0, 0], [0, 1, 0], [1, 0, 1]]
MATRIX_LEFT = [[1, 0, 0], [0, 1, 0], [-1, 0, 1]]

MATRIX_OX = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]
MATRIX_OY = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]

MATRIX_XY = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]

SCALE_X_UP = [[2, 0, 0], [0, 1, 0], [0, 0, 1]]
SCALE_Y_UP = [[1, 0, 0], [0, 2, 0], [0, 0, 1]]

SCALE_X_DOWN = [[0.5, 0, 0], [0, 1, 0], [0, 0, 1]]
SCALE_Y_DOWN = [[1, 0, 0], [0, 0.5, 0], [0, 0, 1]]


def getMatrixTurning(angle: float = np.pi / 3):
    return [[np.cos(angle), np.sin(angle), 0],
            [-np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]]
