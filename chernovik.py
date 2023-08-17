import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

plt.axis('equal')
plt.xlim()
plt.ylim()

def ellips1(A, B, C, D):
    phi = np.linspace(0, 2*np.pi, 500)
    x2, y2 = [], []
    x1 = A * np.cos(phi)
    y1 = B * np.sin(phi)
    n = 0
    for i in x1:
        if -0.6 <= i:
            x2.append(i)
            y2.append(y1[n])
            n += 1
        else:
            n += 1

    x3 = C * np.cos(phi) - 0.7
    y3 = D * np.sin(phi + 20/180*np.pi) - 1.35 + 0.2*np.sin(phi + 20/180*np.pi)

    plt.plot(x2, y2, ',', color='k', )
    plt.plot(x3, y3, ',', color='k')
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('chernovik.png')

for j in np.linspace(0, 2, 500):
    ellips1(j, j/1.05, j/2.5, j/5)