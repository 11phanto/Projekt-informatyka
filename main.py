plik = open('dane.txt')
dane = plik.readlines()
dane = [w.split() for w in dane]

osoba_pin = {int(w[2]): [w[0], w[1], w[3]] for w in dane}

for x in range(1, 4):
    PIN = int(input('Podaj PIN: '))
    if PIN in osoba_pin:
        print('Witaj {}'.format(osoba_pin[PIN][0] + osoba_pin[PIN][1]))
