import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

def randrange(N, vmin, vmax):
    return (vmax - vmin)*np.random.rand(N) + vmin

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
n = 0
k = 0
a = 0
b = 0
c = 0
d = 0
e = 0

N = 10000
xs, ys, zs = [], [], []
x1, y1, z1 = [], [], []
x2, y2, z2 = [], [], []
x3, y3, z3 = [], [], []
x4, y4, z4 = [], [], []
x5, y5, z5 = [], [], []
x6, y6, z6 = [], [], []
x7, y7, z7 = [], [], []

phi = np.linspace(0, 2*np.pi, N)

for m, zlow, zhigh in [(',', -1, 1)]:
    xss = randrange(N, -3.7, 3.7)
    yss = randrange(N, -4.3, 4.3)
    zss = randrange(N, zlow, zhigh)
    for i in xss:
        if i >= -3.2  and (xss[n]**2)/(3.7**2) + (yss[n]**2)/(4.3**2) <= 1:
            xs.append(xss[n])
            ys.append(yss[n])
            zs.append(zss[n])
            n += 1
        else:
            n += 1

    x1s = randrange(N//5, -1, 1)
    y1s = randrange(N//5, -1, 1)
    z1s = randrange(N//5, zlow, zhigh)
    for i in x1s:
        if x1s[a]**2 + y1s[a]**2 <= 1:
            x1.append(x1s[a]-4.1)
            y1.append(y1s[a]-4.6)
            z1.append(z1s[a])
            a += 1
        else:
            a += 1

    x2s = randrange(N, 0, 0.35)
    y2s = randrange(N, 0, 2.6)
    z2s = randrange(N, zlow, zhigh)
    for i in x2s:
        if y2s[k]/(0.35-x2s[k]) <= 2.6/0.35:
            x2.append((x2s[k]**2+y2s[k]**2)**0.5*np.cos(np.arctan(y2s[k]/x2s[k])+2.13)-2.9)
            y2.append((x2s[k]**2+y2s[k]**2)**0.5*np.sin(np.arctan(y2s[k]/x2s[k])+2.13)-1.8)
            z2.append(z2s[k])

            x3.append(((0.35-x2s[k])**2+y2s[k]**2)**0.5*np.cos(np.arctan(y2s[k]/(0.35-x2s[k]))+2.13)-1.7)
            y3.append(((0.35-x2s[k])**2+y2s[k]**2)**0.5*np.sin(np.arctan(y2s[k]/(0.35-x2s[k]))+2.13)-4.1)
            z3.append(z2s[k])
            k += 1
        else:
            k += 1
    
    x4s = randrange(N, 0, 2.5)
    y4s = randrange(N, 0, 2)
    z4s = randrange(N, zlow, zhigh)
    for i in x4s:
        x4.append((x4s[b]**2+y4s[b]**2)**0.5*np.cos(0.56+np.arctan(y4s[b]/x4s[b]))-4.05)
        y4.append((x4s[b]**2+y4s[b]**2)**0.5*np.sin(0.56+np.arctan(y4s[b]/x4s[b]))-4.9)
        z4.append(z4s[b])
        b += 1

    xs5 = randrange(N, -4.4, 4.4)
    ys5 = randrange(N, -5, 5)
    zs5 = randrange(N, zlow, zhigh)
    for i in xs5:
        if i >= -3.6 and (xs5[c]**2)/(4.4**2) + (ys5[c]**2)/(5**2) <= 1:
            x5.append(xs5[c])
            y5.append(ys5[c])
            z5.append(zs5[c])
            c += 1
        else:
            c += 1

    x6s = randrange(N, 0, 3.2)
    y6s = randrange(N, 0, 0.7)
    z6s = randrange(N, zlow, zhigh)    
    for i in x6s:
        if y6s[d]/(3.2-x6s[d]) <= 0.7/3.2:
            x6.append(x6s[d]-3.5)
            y6.append(y6s[d]-5.3)
            z6.append(z6s[d])
            d += 1
        else:
            d += 1

    x7s = randrange(N, 0, 1.5)
    y7s = randrange(N, 0, 0.7)
    z7s = randrange(N, zlow, zhigh)
    for i in x7s:
        if y7s[e]/x7s[e] <= 0.7/1.5:
            x7.append(x7s[e]-5)
            y7.append(y7s[e]-5.3)
            z7.append(z7s[e])
            e += 1
        else:
            e += 1

    ax.scatter(xs, ys, zs, color='black')
    ax.scatter(x1, y1, z1, color='fuchsia')
    ax.scatter(x2, y2, z2, color='darkviolet')
    ax.scatter(x3, y3, z3, color='red')
    ax.scatter(x4, y4, z4, color='yellow')
    ax.scatter(x5, y5, z5, color='c')
    ax.scatter(x6, y6, z6, color='b')
    ax.scatter(x7, y7, z7, color='lime')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.savefig('3d_dich.png')