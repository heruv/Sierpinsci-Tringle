## Introduction

Hi, once I set a goal to write a code in Python that would create a fractal using the so-called game of chaos. I decided to start with a rather simple shape, the Sierpinski triangle.
All I had at the beginning of writing the code was 6 conditions from an article in Wikipedia:

1. Take three points in a plane to form a triangle.
2. Randomly select any point inside the triangle and consider that your current position.
3. Randomly select any one of the three vertex points.
4. Move half the distance from your current position to the selected vertex.
5. Plot the current position.
6. Repeat from step 3.

Since it was proposed to build the triangle using points, it was decided to use matplotlib, which imposed some imprint on the complexity of the mathematical operations used.

Below, the process of building the Sierpinski triangle from the mathematical point of view will be described step by step.

---
## Defining the vertices of the triangle

Based on the definition of the Sierpinski triangle, our triangle, let's call it $ABC$, should be regular, which imposes some difficulties on the definition of the coordinates of the vertices.
If the coordinates of the base vertices are easy to define: $(0, 0)$ for $A$ and $(a, 0)$ for $B$, respectively, then the definition of the coordinates of the vertex $C$ will help us a [rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix). To do this:
1. Set the vector $\vec{AB}$ through the coordinates using this formula $\vec{AB} = (x_B - x_A, y_B - y_A)$.
2. Rotate it by 60 degrees using the rotation matrix.

Thus, the coordinates of the vertex $C$ are:
$$\begin{align*}
C = \vec{AB} \cdot \begin{pmatrix}
\cos \frac{\pi}{3} & -\sin \frac{\pi}{3} \\
\sin \frac{\pi}{3} & \quad \cos \frac{\pi}{3}
\end{pmatrix}.
\end{align*}$$

## Defining a point inside the triangle

In order to define a point (its coordinates) inside the triangle, we will use a quasi-random distribution method (it sounds scary, but in fact, everything is very simple), namely, the [parallelogram method](https://mathworld.wolfram.com/TrianglePointPicking.html). It all comes down to a banal addition of vectors and their reflection if they have gone beyond our triangle.

![alt text](https://habrastorage.org/r/w1560/getpro/habr/post_images/0f1/f04/d28/0f1f04d28a796d7c86d01e60ee33d3e6.png)

To do this, we will need the following formulas:
$$\begin{align*}
\text{if} \quad r_1 + r_2 > 1: \\
P &= ((1 - r_1) \cdot x_{AC} + (1 - r_2) \cdot x_{AB}, (a - r_2) \cdot y_{AC} + (1 - r_2) \cdot y_{AB}); \\
\text{if} \quad r_1 + r_2 < 1: \\
P &= (r_1 \cdot x_{AC} + r_2 \cdot x_{AB}, r_1 \cdot y_{AC} + r_2 \cdot y_{AB}).
\end{align*}$$

## Construction

Now, having completed the first 2 steps, the difficulties end. Since the subsequent steps are quite simple and do not really need explanation (in my opinion), we can move on to the construction of the fractal.

To do this:
1. select a point in the triangle and one of the 3 vertices chosen at random;
2. build a vector defined by coordinates (coordinates of the vertex and our point);
3. divide it by 2;
4. add it to our point (perceive the point as a zero vector);
5. mark the coordinates of the resulting vector on the graph;
6. repeat.

P. S. I had enough 10 thousand points to build it, however, the article in Wikipedia recommends using up to a million points, which is somewhat difficult, since matplotlib.scatter() is not designed for such [a number of points](https://stackoverflow.com/questions/42639129/is-matplotlib-scatter-plot-slow-for-large-number-of-data).
