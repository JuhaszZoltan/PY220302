import module as m

kategoriak = []

for s in open("titanic.txt", encoding='utf-8'):
    kategoriak.append(m.Kategoria(s))

# 2. feladat:
print(f'2. feladat: {len(kategoriak)} db')

# 3. feladat:
print(f'3. feladat: {m.feladat_3(kategoriak)} fő')

# 4.+ 5. feladat:
kulcsszo = input('4. feladat: Kulcsszó: ')
van = m.feladat_4(kategoriak, kulcsszo)
if van:
    print('\tVan találat!')
    print('5. feladat:')
    m.feladat_5(kategoriak, kulcsszo)
else: print('\tNincs találat!')

# 6. feladat:
print('6. feladat:')
for kn in m.feladat_6(kategoriak):
    print(f'\t{kn}')


# 7. feladat:
print(f'7. feladat: {m.feladat_7(kategoriak)}')