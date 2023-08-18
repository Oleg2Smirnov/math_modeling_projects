import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

def ellips1(A, B):
    phi = np.linspace(0, 2*np.pi, 500)
    x2, y2, z2 = [], [], []
    x1 = A * np.outer(phi, np.cos(phi))
    y1 = B * np.outer(phi, np.sin(phi))
    z1 = np.outer(phi/8, np.ones(np.size(phi)))
    n = 0
    for i in (A * np.cos(phi)):
        if -0.6 <= i:
            x2.append(i)
            y2.append(y1[n])
            z2.append(z1[n])
            n += 1
        else:
            n += 1
    ax.plot_surface(x2, y2, z2)
    plt.savefig('3d_dich.png')

for j in np.linspace(0, 2, 500):
    ellips1(j, j/1.05)