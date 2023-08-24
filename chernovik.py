import matplotlib.pyplot as plt
import numpy as np
import init_conditions as incs
def barnard_68(N):
    np.random.seed(19680801) # вообще хз что это, но наверно нужно

    def randrange(N, vmin, vmax):
        return (vmax - vmin)*np.random.rand(N) + vmin  # функция создаёт точки в рандомных местах в указанном диапозоне 

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    n = 0  # используется как номер элемента
    k = 0  # обнуляет n (n=k)

    xs, ys, zs = [], [], []  # тёмный сектор эллипса - центр
    x1, y1, z1 = [], [], []  # малый круг на конце туманности (левый низ)
    x3, y3, z3 = [], [], []  # нижний треугольник трапеции, малое основание которого - диаметр окружности 
    x4, y4, z4 = [], [], []  # прямоугольник трапеции (между треугольниками), соединяет сектор эллипса с окружностью
    x5, y5, z5 = [], [], []  # просвечивающиймя большой сектор эллипса (вокруг тёмного сектора эллипса)
    x6, y6, z6 = [], [], []  # первый треугольник, соединяющий просвечивающуюся часть с малым кругом
    x7, y7, z7 = [], [], []  # второй треугольник, соединяющий просвечивающуюся часть с малым кругом

    # все треугольники являются прямоугольными

    for m, zlow, zhigh in [('.', -R, R)]:
        xss = randrange(N*1000//1313, -3.7, 3.7)
        yss = randrange(N*1000//1313, -4.3, 4.3)
        zss = randrange(N*1000//1313, -0.15, 0.15)
        for i in xss:
            if i >= -3.2  and (xss[n]**2)/(3.7**2) + (yss[n]**2)/(4.3**2) <= 1:
                a = xss[n]
                b = yss[n]
                if a < 0:
                    xs.append(((a**2+b**2)**0.5*np.cos(3.14+0.4636+np.arctan(b/a)))/6)
                    ys.append(((a**2+b**2)**0.5*np.sin(3.14+0.4636+np.arctan(b/a)))/6)
                    zs.append((zss[n]+yss[n])/6)
                    n += 1
                else:
                    xs.append(((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a)))/6)
                    ys.append(((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a)))/6)
                    zs.append((zss[n]+yss[n])/6)
                    n += 1
            else:
                n += 1
        n = k

        x1s = randrange(N*100//2089, -1, 1)
        y1s = randrange(N*100//2089, -1, 1)
        z1s = randrange(N*100//2089, -0.15, 0.15)
        for i in x1s:
            if x1s[n]**2 + y1s[n]**2 <= 1:
                x1.append(((x1s[n]-2.37-0.75))/6)
                y1.append(((y1s[n]-5.326))/6)
                z1.append((z1s[n]+y1s[n]-4.5)/6)
                n += 1
            else:
                n += 1
        n = k

        x3s = randrange(N*1000//91825, 0, 0.35)
        y3s = randrange(N*1000//91825, 0, 2.6)
        z3s = randrange(N*1000//91825, -0.15, 0.15)
        for i in x3s:
            if y3s[n]/(0.35-x3s[n]) <= 2.6/0.35:
                x3.append(((((0.35-x3s[n])**2+y3s[n]**2)**0.5*np.cos(np.arctan(y3s[n]/(0.35-x3s[n]))+2.13+0.4636)+0.317))/6)
                y3.append(((((0.35-x3s[n])**2+y3s[n]**2)**0.5*np.sin(np.arctan(y3s[n]/(0.35-x3s[n]))+2.13+0.4636)-4.43))/6)
                z3.append((z3s[n]+y3s[n]-4.5)/6)
                n += 1
            else:
                n += 1
        n = k

        x4s = randrange(N*100//1671, 0, 2.5)
        y4s = randrange(N*100//1671, 0, 2)
        z4s = randrange(N*100//1671, -0.15, 0.15)
        for i in x4s:
            x4.append((((x4s[n]**2+y4s[n]**2)**0.5*np.cos(0.56+0.4636+np.arctan(y4s[n]/x4s[n]))-1.566))/6)
            y4.append((((x4s[n]**2+y4s[n]**2)**0.5*np.sin(0.56+0.4636+np.arctan(y4s[n]/x4s[n]))-5.93))/6)
            z4.append((z4s[n]+y4s[n]-5)/6)
            n += 1
        n = k

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
                else:                   
                    x5.append(((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a)))/6)
                    y5.append(((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a)))/6)
                    z5.append((z5s[n]+y5s[n])/6)
                    n += 1
            else:
                n += 1                
        n = k

        x6s = randrange(N//373, 0, 3.2)
        y6s = randrange(N//373, 0, 0.7)
        z6s = randrange(N//373, -0.15, 0.15)    
        for i in x6s:
            if y6s[n]/(3.2-x6s[n]) <= 0.7/3.2:
                a = x6s[n]
                b = y6s[n]
                x6.append(((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a))-0.8443)/6)
                y6.append(((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a))-6.324)/6)
                z6.append((z6s[n]+y6s[n]-4.5)/6)
                n += 1
            else:
                n += 1
        n = k

        x7s = randrange(N//1085, 0, 1.1)
        y7s = randrange(N//1085, 0, 0.7)
        z7s = randrange(N//1085, -0.15, 0.15)
        for i in x7s:
            if y7s[n]/x7s[n] <= 0.7/1:
                a = x7s[n]
                b = y7s[n]
                x7.append(((a**2+b**2)**0.5*np.cos(0.4636+np.arctan(b/a))-1.89)/6)
                y7.append(((a**2+b**2)**0.5*np.sin(0.4636+np.arctan(b/a))-6.844)/6)
                z7.append((z7s[n]+y7s[n]-4.5)/6)
                n += 1
            else:
                n += 1

        ax.scatter(xs, ys, zs, color='black', s=2)
        ax.scatter(x1, y1, z1, color='black', s=2)
        ax.scatter(x3, y3, z3, color='black', s=2)
        ax.scatter(x4, y4, z4, color='black', s=2)
        ax.scatter(x5, y5, z5, color='black', s=2)
        ax.scatter(x6, y6, z6, color='black', s=2)
        ax.scatter(x7, y7, z7, color='black', s=2)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        plt.savefig('3d_dich.png')


N = int(input('Введите количество пикселей: '))

barnard_68(N)