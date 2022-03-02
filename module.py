class Kategoria:
    def __init__(self, sor: str):
        v = sor.strip().split(';')
        self.nev = v[0]
        self.tul = int(v[1])
        self.elt = int(v[2])


def feladat_3(kats):
    sum = 0
    for k in kats:
        sum += (k.tul + k.elt)
    return sum


def feladat_4(kats, kulcsszo):
    for k in kats:
        if kulcsszo in k.nev:
            return True
    return False


def feladat_5(kats, kulcsszo):
    for k in kats:
        if kulcsszo in k.nev:
            print(f'\t{k.nev} {k.tul + k.elt} fő')


def feladat_6(kats):
    meghaladja = []
    for k in kats:
        if k.elt > (k.elt + k.tul) * .6:
            meghaladja.append(k.nev)
    return meghaladja


def feladat_7(kats):
    maxi = 0
    for i in range(1, len(kats)):
        if kats[i].tul > kats[maxi].tul:
            maxi = i
    return kats[maxi].nev
