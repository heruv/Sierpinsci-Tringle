import random
import numpy as np
import matplotlib.pyplot as plt


class Fractal:
    def __init__(self, side,):
        self.start_position = None
        self.P = None
        self.targets = None
        self.A = None
        self.B = None
        self.C = None
        self.x = None
        self.y = None
        self.side = side

    def vertex_define(self):
        self.A = np.array([0, 0])
        self.B = np.array([self.side, 0])
        self.C = np.array([self.side / 2, self.side])

        self.x = np.array([self.A[0], self.B[0], self.C[0], self.A[0]])
        self.y = np.array([self.A[1], self.B[1], self.C[1], self.A[1]])

        self.targets = np.array([self.A, self.B, self.C])

    def triangle_point(self):
        r1 = random.random()
        r2 = random.random()

        AC = self.C
        AB = self.B

        if r1 + r2 > 1:  # in auxiliary triangle, perform reflection into target one
            self.P = np.array([(1-r1)*AC[0] + (1-r2)*AB[0], (1-r1)*AC[1] + (1-r2)*AB[1]])
        elif r1 + r2 < 1:
            self.P = np.array([r1*AC[0] + r2*AB[0], r1*AC[1] + r2*AB[1]])

    def move(self):
        target_vertex = random.choice(self.targets)
        self.start_position = [self.P[0], self.P[1]]
        position = []

        for i in range(100):
            movement_distance = np.sqrt(
                (target_vertex[0] - self.start_position[0]) ** 2 + (target_vertex[1] - self.start_position[1]) ** 2) / 2

            self.start_position = [self.start_position[0] + movement_distance,
                                   self.start_position[1] + movement_distance]

            position.append(self.start_position)
        print(position)
        return position


a = Fractal(10)
a.vertex_define()
a.triangle_point()

plt.plot(a.x, a.y)
r1 = []
r2 = []


r1.append(a.move()[0])
r2.append(a.move()[1])

plt.scatter(r1, r2, color='r')
plt.axis('equal')
plt.show()
