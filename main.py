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

print(osoba)
print(' ')

for x in razy:
    razy.append(1)
    print('Dane właściciela konta:')
    print('|| {} '.format(osoba[0] + ' ' + osoba[1]))
    print('|| Twój stan konta wynosi: {} '.format(osoba[-1]))
    if len(his_plat) > 0:
        print('|| Historia transakcji: {} '.format(x for x in his_plat))
    else:
        print('|| Historia transakcji: Brak ')
    odp = input('|| Jaką operację chcesz wykonać? Wypłata / Wpłata / Zakończ \n\n')
    if type(odp) == str:
        if odp.upper() == 'ZAKOŃCZ' or odp.upper() == 'ZAKONCZ':
            print(' ')
            print('Dziękujemy za użycie naszego bankomatu, zapraszamy ponownie.')
            break
        elif odp.upper() == 'WYPŁATA' or odp.upper() == 'WYPLATA':
            print('Wypłata')
            print(' ')
        elif odp.upper() == 'WPŁATA' or odp.upper() == 'WPLATA':
            print('Wpłata')
            print(' ')
        else:
            print('Nie rozpoznano operacji, spróbuj ponownie.')
            print(' ')
    else:
        print('Nie rozpoznano operacji, spróbuj ponownie.')
        print(' ')

