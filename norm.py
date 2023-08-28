import matplotlib.pyplot as plt
import numpy as np
import init_conditions as incs

        
def barnard_68():
    np.random.seed(19680801) # вообще хз что это, но наверно нужно

    def randrange(N, vmin, vmax):
        return (vmax - vmin)*np.random.rand(N) + vmin  # функция создаёт точки в рандомных местах в указанном диапозоне 
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    n = 0  # используется как номер элемента
    k = 0  # обнуляет n (n=k)

    x1, y1, z1 = [], [], [] # тёмный сектор эллипса - центр
    x2, y2, z2 = [], [], [] # малый круг на конце туманности (левый низ)
    x3, y3, z3 = [], [], [] # нижний треугольник трапеции, малое основание которого - диаметр окружности 
    x4, y4, z4 = [], [], [] # прямоугольник трапеции (выше треугольника x3), соединяет сектор эллипса с окружностью
    x5, y5, z5 = [], [], [] # просвечивающиймя большой сектор эллипса (вокруг тёмного сектора эллипса)
    x6, y6, z6 = [], [], [] # первый треугольник, соединяющий просвечивающуюся часть с малым кругом
    x7, y7, z7 = [], [], [] # второй треугольник, соединяющий просвечивающуюся часть с малым кругом

    # все треугольники являются прямоугольными

    for m, zlow, zhigh in [('.', -1, 1)]:
        x1s = randrange(incs.N*1000//incs.S1, -incs.b_ellips1, incs.b_ellips1)
        y1s = randrange(incs.N*1000//incs.S1, -incs.a_ellips1, incs.a_ellips1)
        z1s = randrange(incs.N*1000//incs.S1, -incs.zcoord, incs.zcoord)
        for i in x1s:
            if i >= incs.sector1  and (x1s[n]**2)/(incs.b_ellips1**2) + (y1s[n]**2)/(incs.a_ellips1**2) <= 1:
                x1.append(x1s[n]/incs.miu)
                y1.append(y1s[n]/incs.miu)
                z1.append(z1s[n]/incs.miu)
                n += 1
            else:
                n += 1
        n = k
    
        x2s = randrange(incs.N*100//incs.S2, -incs.Radius, incs.Radius)
        y2s = randrange(incs.N*100//incs.S2, -incs.Radius, incs.Radius)
        z2s = randrange(incs.N*100//incs.S2, -incs.zcoord, incs.zcoord)
        for i in x2s:
            if x2s[n]**2 + y2s[n]**2 <= incs.Radius:
                x2.append(((x2s[n]+incs.X2))/incs.miu)
                y2.append(((y2s[n]+incs.Y2))/incs.miu)
                z2.append(z2s[n]/incs.miu)
                n += 1
            else:
                n += 1
        n = k

        x3s = randrange(incs.N*1000//incs.S3, 0, incs.katetx3)
        y3s = randrange(incs.N*1000//incs.S3, 0, incs.katety3)
        z3s = randrange(incs.N*1000//incs.S3, -incs.zcoord, incs.zcoord)
        for i in x3s:
            if y3s[n]/(incs.katetx3-x3s[n]) <= incs.katety3/incs.katetx3:
                x3.append(((((incs.katetx3-x3s[n])**2+y3s[n]**2)**0.5*np.cos(np.arctan(y3s[n]/(incs.katetx3-x3s[n]))+incs.betta+incs.alpha)+incs.X3))/incs.miu)
                y3.append(((((incs.katetx3-x3s[n])**2+y3s[n]**2)**0.5*np.sin(np.arctan(y3s[n]/(incs.katetx3-x3s[n]))+incs.betta+incs.alpha)+incs.Y3))/incs.miu)
                z3.append(z3s[n]/incs.miu)
                n += 1
            else:
                n += 1
        n = k

        x4s = randrange(incs.N*100//incs.S4, 0, incs.L41)
        y4s = randrange(incs.N*100//incs.S4, 0, incs.L42)
        z4s = randrange(incs.N*100//incs.S4, -incs.zcoord, incs.zcoord)
        for i in x4s:
            x4.append((((x4s[n]**2+y4s[n]**2)**0.5*np.cos(incs.gamma+incs.alpha+np.arctan(y4s[n]/x4s[n]))+incs.X4))/incs.miu)
            y4.append((((x4s[n]**2+y4s[n]**2)**0.5*np.sin(incs.gamma+incs.alpha+np.arctan(y4s[n]/x4s[n]))+incs.Y4))/incs.miu)
            z4.append(z4s[n]/incs.miu)
            n += 1
        n = k

        x5s = randrange(incs.N*10000//incs.S5, -incs.b_ellips5, incs.b_ellips5)
        y5s = randrange(incs.N*10000//incs.S5, -incs.a_ellips5, incs.a_ellips5)
        z5s = randrange(incs.N*10000//incs.S5, -incs.zcoord, incs.zcoord)
        for i in x5s:
            if i >= incs.sector5 and (x5s[n]**2)/(incs.b_ellips5**2) + (y5s[n]**2)/(incs.a_ellips5**2) <= 1:
                x5.append(x5s[n]/incs.miu)
                y5.append(y5s[n]/incs.miu)
                z5.append(z5s[n]/incs.miu)
                n += 1
            else:
                n += 1
        n = k

        x6s = randrange(incs.N//incs.S6, 0, incs.katetx6)
        y6s = randrange(incs.N//incs.S6, 0, incs.katety6)
        z6s = randrange(incs.N//incs.S6, -incs.zcoord, incs.zcoord)    
        for i in x6s:
            if y6s[n]/(incs.katetx6-x6s[n]) <= incs.katety6/incs.katetx6:
                a = x6s[n]
                b = y6s[n]
                x6.append(((a**2+b**2)**0.5*np.cos(incs.alpha+np.arctan(b/a))+incs.X6)/incs.miu)
                y6.append(((a**2+b**2)**0.5*np.sin(incs.alpha+np.arctan(b/a))+incs.Y6)/incs.miu)
                z6.append(z6s[n]/incs.miu)
                n += 1
            else:
                n += 1
        n = k

        x7s = randrange(incs.N//incs.S7, 0, incs.katetx7)
        y7s = randrange(incs.N//incs.S7, 0, incs.katety7)
        z7s = randrange(incs.N//incs.S7, -incs.zcoord, incs.zcoord)
        for i in x7s:
            if y7s[n]/x7s[n] <= incs.katety7/incs.katetx7:
                a = x7s[n]
                b = y7s[n]
                x7.append(((a**2+b**2)**0.5*np.cos(np.arctan(b/a))+incs.X7)/incs.miu)
                y7.append(((a**2+b**2)**0.5*np.sin(np.arctan(b/a))+incs.Y7)/incs.miu)
                z7.append(z7s[n]/incs.miu)
                n += 1
            else:
                n += 1

    coords = []
    b = []
    for j in np.arange(1, 8, 1):
        if j == 1:
            for i in np.arange(0, len(x1), 1):
                a = [x1[i], y1[i], z1[i]]
                coords.append(a)
        if j == 2:
            for i in np.arange(0, len(x2), 1):
                a = [x2[i], y2[i], z2[i]]
                coords.append(a)
        if j == 3:
            for i in np.arange(0, len(x3), 1):
                a = [x3[i], y3[i], z3[i]]
                coords.append(a)
        if j == 4:
            for i in np.arange(0, len(x4), 1):
                a = [x4[i], y4[i], z4[i]]
                coords.append(a)
        if j == 5:
            for i in np.arange(0, len(x5), 1):
                a = [x5[i], y5[i], z5[i]]
                coords.append(a)
        if j == 6:
            for i in np.arange(0, len(x6), 1):
                a = [x6[i], y6[i], z6[i]]
                coords.append(a)
        if j == 7:
            for i in np.arange(0, len(x7), 1):
                a = [x7[i], y7[i], z7[i]]
                coords.append(a)
    return np.array(coords)

barnard_68()