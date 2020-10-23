import numpy as np

class Camera:

    def __init__(self, res=(1920, 1080), aspect=(16, 9), handler=None):
        self.resolution = res
        self.aspect = aspect
        self.handler = handler
        self.translation, self.rotation, self.essential, self.centerCamera = None, None, None, None

    def calcVecsFromEssential(self, essential, centerCamera):
        self.essential = essential
        self.centerCamera = centerCamera
        U, S, V = np.linalg.svd(essential)
        Z = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 0]])
        W = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        Ut = np.transpose(U)
        T = np.matmul(U, np.matmul(Z, Ut))
        Vt = np.transpose(V)
        R = np.matmul(U, np.matmul(W, Vt))