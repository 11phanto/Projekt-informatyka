plik = open('dane.txt')
dane = plik.readlines()
dane = [w.split() for w in dane]

osoba_pin = {int(w[2]): [w[0], w[1], w[3]] for w in dane}

for x in range(1, 4):
    PIN = int(input('Podaj PIN (x0, x0): '))
    print(' ')
    if PIN in osoba_pin:
        print('Witaj {}'.format(osoba_pin[PIN][0] + ' ' + osoba_pin[PIN][1] + '!'))
        print(' ')
        osoba = osoba_pin[PIN]
        break
    elif x < 3:
        print('Masz jeszcze {} szans!'.format(3 - x))
    else:
        print('Brak dostępu! - Szanse się skończyły.')
        exit()

srodki_bankomat = 4500

razy = [1]
his_plat = []

for x in razy:
    razy.append(1)
    print('|| {} '.format(osoba[0] + ' ' + osoba[1]))
    print('|| Twój stan konta wynosi: {} '.format(osoba[-1]))
    if len(his_plat) > 0:
        print('|| Historia transakcji: {} '.format(x for x in his_plat))
    else:
        print('|| Historia transakcji: Brak ')
    odp = input('|| Jaką operację chcesz wykonać? Wypłata / Wpłata / Zakończ \n\n')
    if type(odp) == type(1) or type(odp) == type(1.5):
        print('Nie rozpoznano operacji, spróbój ponownie.')
        print(' ')
    if odp == 'Zakończ':
        print(' ')
        print('Dziękujemy za użycie naszego bankomatu, zapraszamy ponownie.')
        break

#print('|| Historia płatności: {}'.format(x for x in his_plat if len(his_plat) > 0))