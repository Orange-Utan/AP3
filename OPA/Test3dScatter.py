import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

n = 100

def f(n,m):
    return m**2+n**2-n*m*(n+m)


# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
i = 0
j = 0
for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = i
    ys = j
    zs = f(xs,ys)
    ax.scatter(xs, ys, zs, marker=m)
    i+=1
    j+=1

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()