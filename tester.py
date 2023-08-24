import matplotlib.pyplot as plt
import numpy as np

def barnard_68(N):
    np.random.seed(19680801)

    def randrange(N, vmin, vmax):
        return (vmax - vmin)*np.random.rand(N) + vmin

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    n = 0
    k = 0

    xs, ys, zs = [], [], []
    x1, y1, z1 = [], [], []
    x2, y2, z2 = [], [], []
    x3, y3, z3 = [], [], []
    x4, y4, z4 = [], [], []
    x5, y5, z5 = [], [], []
    x6, y6, z6 = [], [], []
    x7, y7, z7 = [], [], []

    for m, zlow, zhigh in [(',', -1, 1)]:
        xss = randrange(N*1000//1313, -3.7, 3.7)
        yss = randrange(N*1000//1313, -4.3, 4.3)
        zss = randrange(N*1000//1313, 0, 0.3)
        for i in xss:
            if i >= -3.2  and (xss[n]**2)/(3.7**2) + (yss[n]**2)/(4.3**2) <= 1:
                xs.append(xss[n])
                ys.append(yss[n])
                zs.append(zss[n])
                n += 1
            else:
                n += 1
        n = k
        x1s = randrange(N*100//2089, -1, 1)
        y1s = randrange(N*100//2089, -1, 1)
        z1s = randrange(N*100//2089, 0, 0.3)
        for i in x1s:
            if x1s[n]**2 + y1s[n]**2 <= 1:
                x1.append((x1s[n]-4.5))
                y1.append((y1s[n]-3.7))
                z1.append(z1s[n])
                n += 1
            else:
                n += 1
        n = k
        x2s = randrange(N*1000//91825, 0, 0.35)
        y2s = randrange(N*1000//91825, 0, 2.6)
        z2s = randrange(N*1000//91825, 0, 0.3)
        for i in x2s:
            if y2s[n]/(0.35-x2s[n]) <= 2.6/0.35:
                x2.append(((x2s[n]**2+y2s[n]**2)**0.5*np.cos(np.arctan(y2s[n]/x2s[n])+2.13)-2.9))
                y2.append(((x2s[n]**2+y2s[n]**2)**0.5*np.sin(np.arctan(y2s[n]/x2s[n])+2.13)-1.8))
                z2.append(z2s[n])

                x3.append((((0.35-x2s[n])**2+y2s[n]**2)**0.5*np.cos(np.arctan(y2s[n]/(0.35-x2s[n]))+2.13)-1.7))
                y3.append((((0.35-x2s[n])**2+y2s[n]**2)**0.5*np.sin(np.arctan(y2s[n]/(0.35-x2s[n]))+2.13)-4.1))
                z3.append(z2s[n])
                n += 1
            else:
                n += 1
        n = k
        x4s = randrange(N*100//1671, 0, 2.5)
        y4s = randrange(N*100//1671, 0, 2)
        z4s = randrange(N*100//1671, 0, 0.3)
        for i in x4s:
            x4.append(((x4s[n]**2+y4s[n]**2)**0.5*np.cos(0.56+np.arctan(y4s[n]/x4s[n]))-4.05))
            y4.append(((x4s[n]**2+y4s[n]**2)**0.5*np.sin(0.56+np.arctan(y4s[n]/x4s[n]))-4.6))
            z4.append(z4s[n])
            n += 1
        n = k
        xs5 = randrange(N*10000//94955, -4.4, 4.4)
        ys5 = randrange(N*10000//94955, -5, 5)
        zs5 = randrange(N*10000//94955, 0, 0.3)
        for i in xs5:
            if i >= -3.6 and (xs5[n]**2)/(4.4**2) + (ys5[n]**2)/(5**2) <= 1:
                x5.append(xs5[n])
                y5.append(ys5[n])
                z5.append(zs5[n])
                n += 1
            else:
                n += 1
        n = k
        x6s = randrange(N//373, 0, 3.2)
        y6s = randrange(N//373, 0, 0.7)
        z6s = randrange(N//373, 0, 0.3)    
        for i in x6s:
            if y6s[n]/(3.2-x6s[n]) <= 0.7/3.2:
                x6.append((x6s[n]-3.5))
                y6.append((y6s[n]-5.2))
                z6.append(z6s[n])
                n += 1
            else:
                n += 1
        n = k
        x7s = randrange(N//1085, 0, 1.1)
        y7s = randrange(N//1085, 0, 0.7)
        z7s = randrange(N//1085, 0, 0.3)
        for i in x7s:
            if y7s[n]/x7s[n] <= 0.7/1:
                x7.append((x7s[n]-4.7))
                y7.append((y7s[n]-5.3))
                z7.append(z7s[n])
                n += 1
            else:
                n += 1
    ax.scatter(xs, ys, zs, color='black')
    ax.scatter(x1, y1, z1, color='black')
    ax.scatter(x2, y2, z2, color='black')
    ax.scatter(x3, y3, z3, color='black')
    ax.scatter(x4, y4, z4, color='black')
    ax.scatter(x5, y5, z5, color='black')
    ax.scatter(x6, y6, z6, color='black')
    ax.scatter(x7, y7, z7, color='black')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.savefig('3d_dich.png')


N = int(input('Введите количество пикселей: '))

barnard_68(N)




                x2.append((((x2s[n]**2+y2s[n]**2)**0.5*np.cos(np.arctan(y2s[n]/x2s[n])+2.13+0.4636)-1.7526))/6)
                y2.append((((x2s[n]**2+y2s[n]**2)**0.5*np.sin(np.arctan(y2s[n]/x2s[n])+2.13+0.4636)-2.84))/6)
                z2.append((z2s[n]+y2s[n]-4.5)/6)