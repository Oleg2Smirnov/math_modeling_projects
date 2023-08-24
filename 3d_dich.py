import matplotlib.pyplot as plt
import numpy as np

def randrange(N, vmin, vmax):
        return (vmax - vmin)*np.random.rand(N) + vmin

def graphical_output():
    pass
        
def barnard_68(N):
    np.random.seed(19680801)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    n = 0
    k = 0
    h = 0

    xs, ys, zs = [], [], []
    x1, y1, z1 = [], [], []
    x2, y2, z2 = [], [], []
    x3, y3, z3 = [], [], []
    x4, y4, z4 = [], [], []
    x5, y5, z5 = [], [], []
    x6, y6, z6 = [], [], []
    x7, y7, z7 = [], [], []

    for m, zlow, zhigh in [('.', -1, 1)]:
        xss = randrange(N*1000//1313, -3.7, 3.7)
        yss = randrange(N*1000//1313, -4.3, 4.3)
        zss = randrange(N*1000//1313, -0.15, 0.15)
        for i in xss:
            if i >= -3.2  and (xss[n]**2)/(3.7**2) + (yss[n]**2)/(4.3**2) <= 1:
                a = xss[n]
                b = yss[n]
                c = zss[n]
                if a < 0:
                    xs.append(((a**2+b**2)**0.5*np.cos(3.14+0.4636+np.arctan(b/a)))/6)
                    ys.append(((a**2+b**2)**0.5*np.sin(3.14+0.4636+np.arctan(b/a)))/6)
                    zs.append((zss[n]+yss[n])/6)
                    a = xs[h]
                    b = ys[h]

                    n += 1
                    h += 1
                else:
                    xs.append(((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a)))/6)
                    ys.append(((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a)))/6)
                    zs.append((zss[n]+yss[n])/6)

                    n += 1
                    h += 1
            else:
                n += 1
        n = k
        h = k
        x1s = randrange(N*100//2089, -1.1, 1.1)
        y1s = randrange(N*100//2089, -1.1, 1.1)
        z1s = randrange(N*100//2089, -0.15, 0.15)
        for i in x1s:
            if x1s[n]**2 + y1s[n]**2 <= 1.2:
                x1.append(((x1s[n]-2.37-0.85))/6)
                y1.append(((y1s[n]-5.326+1.2))/6)
                z1.append((z1s[n]+y1s[n]-4.5)/6)

                n += 1
                h += 1
            else:
                n += 1
        n = k
        h = k
        x2s = randrange(N*1000//91825, 0, 0.35)
        y2s = randrange(N*1000//91825, 0, 2.6)
        z2s = randrange(N*1000//91825, -0.15, 0.15)
        for i in x2s:
            if y2s[n]/(0.35-x2s[n]) <= 2.6/0.35:
                x2.append((((x2s[n]**2+y2s[n]**2)**0.5*np.cos(np.arctan(y2s[n]/x2s[n])+2.13+0.4636)-1.7526))/6)
                y2.append((((x2s[n]**2+y2s[n]**2)**0.5*np.sin(np.arctan(y2s[n]/x2s[n])+2.13+0.4636)+1.2-2.84))/6)
                z2.append((z2s[n]+y2s[n]-4.5)/6)
                a = x2[h]
                b = y2[h]
                c = z2s[n]


                x3.append(((((0.35-x2s[n])**2+y2s[n]**2)**0.5*np.cos(np.arctan(y2s[n]/(0.35-x2s[n]))+2.13+0.4636)+0.317-0.2))/6)
                y3.append(((((0.35-x2s[n])**2+y2s[n]**2)**0.5*np.sin(np.arctan(y2s[n]/(0.35-x2s[n]))+2.13+0.4636)-4.43+1.2-0.2))/6)
                z3.append((z2s[n]+y2s[n]-4.5)/6)

                n += 1
                h += 1
            else:
                n += 1
        n = k
        h = k
        x4s = randrange(N*100//1671, 0, 2.5)
        y4s = randrange(N*100//1671, 0, 2)
        z4s = randrange(N*100//1671, -0.15, 0.15)
        for i in x4s:
            x4.append((((x4s[n]**2+y4s[n]**2)**0.5*np.cos(0.56+0.4636+np.arctan(y4s[n]/x4s[n]))-1.566))/6)
            y4.append((((x4s[n]**2+y4s[n]**2)**0.5*np.sin(0.56+0.4636+np.arctan(y4s[n]/x4s[n]))-5.93+0.6))/6)
            z4.append((z4s[n]+y4s[n]-4.5)/6)

            n += 1
            h += 1
        n = k
        h = k
        x5s = randrange(N*10000//94955, -4.4, 4.4)
        y5s = randrange(N*10000//94955, -5, 5)
        z5s = randrange(N*10000//94955, -0.15, 0.15)
        for i in x5s:
            if i >= -3.6 and (x5s[n]**2)/(4.4**2) + (y5s[n]**2)/(5**2) <= 1:
                a = x5s[n]
                b = y5s[n]
                if a < 0:
                    x5.append(((a**2+b**2)**0.5*np.cos(0.4636+3.14+np.arctan(b/a)))/6)
                    y5.append(((a**2+b**2)**0.5*np.sin(0.4636+3.14+np.arctan(b/a)))/6)
                    z5.append((z5s[n]+y5s[n])/6)

                    n += 1
                    h += 1
                else:                   
                    x5.append(((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a)))/6)
                    y5.append(((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a)))/6)
                    z5.append((z5s[n]+y5s[n])/6)

                    n += 1
                    h += 1
            else:
                n += 1
        n = k
        h = k
        x6s = randrange(N//373, 0, 3.2)
        y6s = randrange(N//373, 0, 0.7)
        z6s = randrange(N//373, -0.15, 0.15)    
        for i in x6s:
            if y6s[n]/(3.2-x6s[n]) <= 0.7/3.2:
                a = x6s[n]
                b = y6s[n]
                x6.append(((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a))-0.8443)/6)
                y6.append(((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a))-6.324+1.2)/6)
                z6.append((z6s[n]+y6s[n]-4.5)/6)

                n += 1
                h += 1
            else:
                n += 1
        n = k
        h = k
        x7s = randrange(N//1085, 0, 1.1)
        y7s = randrange(N//1085, 0, 0.7)
        z7s = randrange(N//1085, -0.15, 0.15)
        for i in x7s:
            if y7s[n]/x7s[n] <= 0.7/1:
                a = x7s[n]
                b = y7s[n]
                x7.append(((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a))-1.89)/6)
                y7.append(((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a))-6.844+1.2)/6)
                z7.append((z7s[n]+y7s[n]-4.5)/6)
                a = x7[h]
                b = y7[h]
                c = z7s[n]

                n += 1
                h += 1
            else:
                n += 1

        ax.scatter(xs, ys, zs, color='black', s=1)
        ax.scatter(x1, y1, z1, color='black', s=1)
        ax.scatter(x3, y3, z3, color='black', s=1)
        ax.scatter(x4, y4, z4, color='black', s=1)
        ax.scatter(x5, y5, z5, color='black', s=1)
        ax.scatter(x6, y6, z6, color='black', s=1)
        ax.scatter(x7, y7, z7, color='black', s=1)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        plt.savefig('3d_dich.png')


N = int(input('Введите количество пикселей: '))

barnard_68(N)