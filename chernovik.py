if a >= 0 and b >= 0 and b/a >= 1/3:
    z.append(z + (x**2+y**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
elif a <= 0 and b <= 0 and a/b >= 3:
    z.append(z + (x**2+y**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
elif a <= 0 and b >= 0:
    z.append(z + (x**2+y**2)**0.5 * np.cos(1.249-np.arctan(b/a)))
