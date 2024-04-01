plik = open('dane.txt')
dane = plik.readlines()
dane = [w.split() for w in dane]

osoba_pin = {int(w[2]): [w[0], w[1], w[3]] for w in dane}

for x in range(1, 4):
    PIN = int(input('Podaj PIN: '))
    if PIN in osoba_pin:
        print('Witaj {}'.format(osoba_pin[PIN][0] + ' ' + osoba_pin[PIN][1] + '!'))
        osoba = osoba_pin[PIN]
        break
    elif x < 3:
        print('Masz jeszcze {} szans!'.format(3 - x))
    else:
        print('Brak dostępu! - Szanse się skończyły.')

srodki_bankomat = 4500

razy = [1]
for x in razy:
    razy.append(1)
    print('|| {}'.format(osoba[0] + ' ' + osoba[1]))
    print('|| Twój stan konta wynosi: {}'.format(osoba[-1]))
    odp = input('|| Jaką operację chcesz wykonać? Wypłata / Wpłata \n\n')
    break