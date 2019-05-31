import random

Vth = 0 #
Xt = random.randint(0, 100)
Ln = 0
i = 0
V = list()
length = len(Xt)
while i <= length:
    Vmax = Vmin = Xt[i]
    Vmax1 = Vmin1 = Xt[i]
    i = i + 1
    while Ln <= 50:
        Ln = Ln + 1
        if Xt[i] > Vmax: 
            Vmax1 = Xt[i]
        elif Xt[i] < Vmin:
            Vmin1 = Xt[i]
        else:
            i += 1

        if Vmax1 - Vmin1 > Vth:
            delV = ((Vmax1 - Vmin1) - Vth)
            Vth += delV
            for j in range(Ln):
                V.append((Vmax + Vmin)/2)
            Ln = 0
            break
        else:
            Vmax = Vmax1 
            Vmin = Vmin1

print(V)


