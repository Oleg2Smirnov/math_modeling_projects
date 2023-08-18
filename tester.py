import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


def randrange(N, vmin, vmax):
    return (vmax - vmin)*np.random.rand(N) + vmin

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
n = 0
N = 1000
xs, ys, zs = [], [], []
phi = np.linspace(0, 2*np.pi, 1000)
for m, zlow, zhigh in [(',', -1, 1)]:
    xss = randrange(N, -3.7*np.cos(phi), 3.7*np.cos(phi))
    yss = randrange(N, -4.3*np.sin(phi), 4.3*np.sin(phi))
    zss = randrange(N, zlow, zhigh)
    for i in xss:
        if i >= -3.2:
            xs.append(xss[n])
            ys.append(yss[n])
            zs.append(zss[n])
            n += 1
        else:
            n += 1


    
for m, zlow, zhigh in [(',', -1, 1)]:
    x1 = randrange(N, -1*np.cos(phi)-4.1, 1*np.cos(phi)-4.1)
    y1 = randrange(N, -1*np.sin(phi)-4.1, 1*np.sin(phi)-4.1)
    z1 = randrange(N, zlow, zhigh)

    ax.scatter(xs, ys, zs, color='black')
    ax.scatter(x1, y1, z1, color='black')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.savefig('3d_dich.png')