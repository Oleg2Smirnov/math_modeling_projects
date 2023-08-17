import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

plt.axis('equal')
plt.xlim()
plt.ylim()

def ellips1(A, B):
    phi = np.linspace(0, 2*np.pi, 500)
    x2 = []
    y2 = []
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


    plt.plot(x2, y2, label='ellips1', color='k')
    plt.legend()
    plt.xlabel('x - coord')
    plt.ylabel('y - coord')
    plt.savefig('ellips.png')

for j in np.linspace(0, 2, 100):
    ellips1(j, j/1.05)