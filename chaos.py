import random
import numpy as np
import matplotlib.pyplot as plt


class Fractal:
    def __init__(self, side, ):
        self.start_position = None
        self.targets = None
        self.A = None
        self.B = None
        self.C = None
        self.side = side

    def _rotate(self, vector: np.array, angle: int):
        angle = np.deg2rad(angle)
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
        ])

        rotated_vector = rotation_matrix.dot(vector)
        rotated_vector[0], rotated_vector[1] = (np.round(rotated_vector[0], 4),
                                                np.round(rotated_vector[1], 4))
        return rotated_vector

    def vertex_define(self):
        self.A = np.array([0, 0])
        self.B = np.array([self.side, 0])
        self.C = self._rotate(np.array([self.side - 0, 0]), 60)

        self.targets = np.array([self.A, self.B, self.C])

    def get_point_on_triangle(self):
        r1 = random.random()
        r2 = random.random()

        AC = self.C
        AB = self.B

        if r1 + r2 > 1:  # in auxiliary triangle, perform reflection into target one
            Point = np.array([(1 - r1) * AC[0] + (1 - r2) * AB[0], (1 - r1) * AC[1] + (1 - r2) * AB[1]])
        elif r1 + r2 < 1:
            Point = np.array([r1 * AC[0] + r2 * AB[0], r1 * AC[1] + r2 * AB[1]])

        self.start_position = [Point[0], Point[1]]

    def move(self):
        target_vertex = random.choice(self.targets)

        movement_distance = np.array([(target_vertex[0] - self.start_position[0]) / 2,
                                      (target_vertex[1] - self.start_position[1]) / 2])

        self.start_position = [self.start_position[0] + movement_distance[0],
                               self.start_position[1] + movement_distance[1]]

        position = self.start_position

        return position


a = Fractal(5)
a.vertex_define()
a.get_point_on_triangle()

plt.grid(True, which='major', linewidth=1.2)
r1 = []
r2 = []
points = []

for i in range(10_000):
    points = a.move()
    r1.append(points[0])
    r2.append(points[1])

plt.scatter(r1, r2, s=5, color='r', marker="^")
plt.axis('equal')
plt.show()
