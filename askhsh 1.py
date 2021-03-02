import secrets

x = int(input("dwse thn diastash tou tetragwnou:"))
while x < 4:
    print("dwse megaliterh diastash")
    x = int(input("dwse thn diastash tou tetragwnou:"))

sinolo = x ** 2

if x % 2 == 1:
    theseis_asswn = round(sinolo / 2) + 1
else:
    theseis_asswn = round(sinolo / 2)
upoloipes_theseis = sinolo - theseis_asswn

athroisma = 0
for a in range(10):
    arithmoi = [0, 1]
    mon = 0
    mhden = 0
    pinakas = []
    for b in range(x):
        gemisma = []
        for c in range(x):
            tux_ar = secrets.choice(arithmoi)
            if tux_ar == 1 and mon < theseis_asswn:
                gemisma.append(tux_ar)
                mon += 1
            elif tux_ar == 0 and mhden < upoloipes_theseis:
                gemisma.append(tux_ar)
                mhden += 1
            elif mon == theseis_asswn:
                gemisma.append(0)
            elif mhden == upoloipes_theseis:
                gemisma.append(1)
        pinakas.append(gemisma)
    orizontia = 0
    katheta = 0
    diagwnia = 0
    for i in range(x):
        for j in range(0, x - 3):
            if pinakas[i][j] == pinakas[i][j + 1] == pinakas[i][j + 2] == pinakas[i][j + 3] == 1:
                orizontia += 1
    for i in range(0, x - 3):
        for j in range(x):
            if pinakas[i][j] == pinakas[i + 1][j] == pinakas[i + 2][j] == pinakas[i + 3][j] == 1:
                katheta += 1
    for i in range(0, x - 3):
        for j in range(0, x - 3):
            if i == j:
                if pinakas[i][j] == pinakas[i + 1][j + 1] == pinakas[i + 2][j + 2] == pinakas[i + 3][j + 3] == 1:
                    diagwnia += 1
    m = 0
    for i in range(0, x - 3):
        for j in range(3, x):
            if i + j == x + 1:
                if pinakas[i][j] == 1:
                   m += 1
                else:
                    m = 0
            if m == 4:
                diagwnia += 1
                m = 0
    k = 1
    while k != x:
        p = 0
        for i in range(x):
            for j in range(x):
                if j == i+k:
                    if pinakas[i][j] == 1:
                        p += 1
                    else:
                        p = 0
                if p == 4:
                    diagwnia += 1
                    p = 0
        k += 1
    k = 1
    while k != x:
        p = 0
        for j in range(x):
            for i in range(x):
                if i == j + k:
                    if pinakas[i][j] == 1:
                        p += 1
                    else:
                        p = 0
                if p == 4:
                    diagwnia += 1
                    p = 0
        k += 1
    for i in range(x):
        for j in range(x):
            if i == x - 4 and j == x - 4:
                if pinakas[i][j] == pinakas[i + 1][j - 1] == pinakas[i + 2][j - 2] == pinakas[i + 3][j - 3] == 1:
                    diagwnia += 1
    athroisma = orizontia + katheta + diagwnia
    print (athroisma)
    mesos_oros = athroisma/100
    print(mesos_oros)


