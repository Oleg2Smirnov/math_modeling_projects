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
    h = 0

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
                a = xss[n]
                b = yss[n]
                c = zss[n]
                if a < 0:
                    xs.append((a**2+b**2)**0.5*np.cos(3.14+0.4636+np.arctan(b/a)))
                    ys.append((a**2+b**2)**0.5*np.sin(3.14+0.4636+np.arctan(b/a)))
                    a = xs[h]
                    b = ys[h]
                    if a >= 0 and b >= 0 and b/a >= 1/3:
                        zs.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    elif a <= 0 and b <= 0 and a/b >= 3:
                        zs.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    elif a <= 0 and b >= 0:
                        zs.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    else:
                        zs.append(c - (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    n += 1
                    h += 1
                else:
                    xs.append((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a)))
                    ys.append((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a)))
                    a = xs[h]
                    b = ys[h]
                    if a >= 0 and b >= 0 and b/a >= 1/3:
                        zs.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    elif a <= 0 and b <= 0 and a/b >= 3:
                        zs.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    elif a <= 0 and b >= 0:
                        zs.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    else:
                        zs.append(c - (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    n += 1
                    h += 1
            else:
                n += 1
        n = k
        h = k
        x1s = randrange(N*100//2089, -1, 1)
        y1s = randrange(N*100//2089, -1, 1)
        z1s = randrange(N*100//2089, 0, 0.3)
        for i in x1s:
            if x1s[n]**2 + y1s[n]**2 <= 1:
                x1.append((x1s[n]-2.37))
                y1.append((y1s[n]-5.326))
                a = x1[h]
                b = y1[h]
                c = z1s[h]
                if a >= 0 and b >= 0 and b/a >= 1/3:
                    z1.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                elif a <= 0 and b <= 0 and a/b >= 3:
                    z1.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                elif a <= 0 and b >= 0:
                    z1.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                else:
                    z1.append(c - (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                n += 1
                h += 1
            else:
                n += 1
        n = k
        h = k
        x2s = randrange(N*1000//91825, 0, 0.35)
        y2s = randrange(N*1000//91825, 0, 2.6)
        z2s = randrange(N*1000//91825, 0, 0.3)
        for i in x2s:
            if y2s[n]/(0.35-x2s[n]) <= 2.6/0.35:
                x2.append(((x2s[n]**2+y2s[n]**2)**0.5*np.cos(np.arctan(y2s[n]/x2s[n])+2.13+0.4636)-1.7526))
                y2.append(((x2s[n]**2+y2s[n]**2)**0.5*np.sin(np.arctan(y2s[n]/x2s[n])+2.13+0.4636)-2.84))
                a = x2[h]
                b = y2[h]
                c = z2s[n]
                if a >= 0 and b >= 0 and b/a >= 1/3:
                    z2.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                elif a <= 0 and b <= 0 and a/b >= 3:
                    z2.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                elif a <= 0 and b >= 0:
                    z2.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                else:
                    z2.append(c - (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))

                x3.append((((0.35-x2s[n])**2+y2s[n]**2)**0.5*np.cos(np.arctan(y2s[n]/(0.35-x2s[n]))+2.13+0.4636)+0.317))
                y3.append((((0.35-x2s[n])**2+y2s[n]**2)**0.5*np.sin(np.arctan(y2s[n]/(0.35-x2s[n]))+2.13+0.4636)-4.43))
                a = x3[h]
                b = y3[h]
                if a >= 0 and b >= 0 and b/a >= 1/3:
                    z3.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                elif a <= 0 and b <= 0 and a/b >= 3:
                    z3.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                elif a <= 0 and b >= 0:
                    z3.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                else:
                    z3.append(c - (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                n += 1
                h += 1
            else:
                n += 1
        n = k
        h = k
        x4s = randrange(N*100//1671, 0, 2.5)
        y4s = randrange(N*100//1671, 0, 2)
        z4s = randrange(N*100//1671, 0, 0.3)
        for i in x4s:
            x4.append(((x4s[n]**2+y4s[n]**2)**0.5*np.cos(0.56+0.4636+np.arctan(y4s[n]/x4s[n]))-1.566))
            y4.append(((x4s[n]**2+y4s[n]**2)**0.5*np.sin(0.56+0.4636+np.arctan(y4s[n]/x4s[n]))-5.93))
            a = x4[h]
            b = y4[h]
            c = z4s[n]
            if a >= 0 and b >= 0 and b/a >= 1/3:
                z4.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
            elif a <= 0 and b <= 0 and a/b >= 3:
                z4.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
            elif a <= 0 and b >= 0:
                z4.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
            else:
                z4.append(c - (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
            n += 1
            h += 1
        n = k
        h = k
        xs5 = randrange(N*10000//94955, -4.4, 4.4)
        ys5 = randrange(N*10000//94955, -5, 5)
        zs5 = randrange(N*10000//94955, 0, 0.3)
        for i in xs5:
            if i >= -3.6 and (xs5[n]**2)/(4.4**2) + (ys5[n]**2)/(5**2) <= 1:
                a = xs5[n]
                b = ys5[n]
                if a < 0:
                    x5.append((a**2+b**2)**0.5*np.cos(0.4636+3.14+np.arctan(b/a)))
                    y5.append((a**2+b**2)**0.5*np.sin(0.4636+3.14+np.arctan(b/a)))
                    a = x5[h]
                    b = y5[h]
                    c = zs5[n]
                    if a >= 0 and b >= 0 and b/a >= 1/3:
                        z5.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    elif a <= 0 and b <= 0 and a/b >= 3:
                        z5.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    elif a <= 0 and b >= 0:
                        z5.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    else:
                        z5.append(c - (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    n += 1
                    h += 1
                else:                   
                    x5.append((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a)))
                    y5.append((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a)))
                    a = x5[h]
                    b = y5[h]
                    c = zs5[n]
                    if a >= 0 and b >= 0 and b/a >= 1/3:
                        z5.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    elif a <= 0 and b <= 0 and a/b >= 3:
                        z5.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    elif a <= 0 and b >= 0:
                        z5.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    else:
                        z5.append(c - (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                    n += 1
                    h += 1
            else:
                n += 1
        n = k
        h = k
        x6s = randrange(N//373, 0, 3.2)
        y6s = randrange(N//373, 0, 0.7)
        z6s = randrange(N//373, 0, 0.3)    
        for i in x6s:
            if y6s[n]/(3.2-x6s[n]) <= 0.7/3.2:
                a = x6s[n]
                b = y6s[n]
                x6.append((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a))-0.8443)
                y6.append((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a))-6.324)
                a = x6[h]
                b = y6[h]
                c = z6s[n]
                if a >= 0 and b >= 0 and b/a >= 1/3:
                    z6.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                elif a <= 0 and b <= 0 and a/b >= 3:
                    z6.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                elif a <= 0 and b >= 0:
                    z6.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                else:
                    z6.append(c - (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                n += 1
                h += 1
            else:
                n += 1
        n = k
        h = k
        x7s = randrange(N//1085, 0, 1.1)
        y7s = randrange(N//1085, 0, 0.7)
        z7s = randrange(N//1085, 0, 0.3)
        for i in x7s:
            if y7s[n]/x7s[n] <= 0.7/1:
                a = x7s[n]
                b = y7s[n]
                x7.append((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a))-1.89)
                y7.append((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a))-6.844)
                a = x7[h]
                b = y7[h]
                c = z7s[n]
                if a >= 0 and b >= 0 and b/a >= 1/3:
                    z7.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                elif a <= 0 and b <= 0 and a/b >= 3:
                    z7.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                elif a <= 0 and b >= 0:
                    z7.append(c + (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                else:
                    z7.append(c - (a**2+b**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
                n += 1
                h += 1
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