import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

def randrange(N, vmin, vmax):
    return (vmax - vmin)*np.random.rand(N) + vmin

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
n = 0
k = 0
N = 1000
xs, ys, zs = [], [], []
x2, y2, z2 = [], [], []

phi = np.linspace(0, 2*np.pi, N)
theta = np.linspace(0, 2*np.pi, N//5)
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
    x1 = randrange(N//5, -1*np.cos(theta)-4.1, 1*np.cos(theta)-4.1)
    y1 = randrange(N//5, -1*np.sin(theta)-4.1, 1*np.sin(theta)-4.1)
    z1 = randrange(N//5, zlow, zhigh)

for m, zlow, zhigh in [(',', -1, 1)]:
    x2s = randrange(N, 0, 0.35)
    y2s = randrange(N, 0, 2.5)
    z2s = randrange(N, zlow, zhigh)

    for i in x2:
        if (x2s[k]**2 + y2s[k]**2)**0.5 <= 2*y2s[k]/x2s[k]*2.5/0.35/(y2s[k]+2.5/0.35)/
            x2.append((x2s[k]+0.1)*np.cos(2.14326))
            y2.append((y2s[k]+3.5)*np.sin(2.14326))
            z2.append(z2s[k])
            k += 1
        else:
            k += 1

    ax.scatter(xs, ys, zs, color='black')
    ax.scatter(x1, y1, z1, color='black')
    ax.scatter(x2, y2, z2, color='black')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.savefig('3d_dich.png')