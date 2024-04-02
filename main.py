plik = open('dane.txt')
dane = plik.readlines()
dane = [w.split() for w in dane]

osoba_pin = {int(w[2]): [w[0], w[1], w[3]] for w in dane}

for x in range(1, 4):
    PIN = int(input('Podaj PIN (x0, x0): '))
    if PIN in osoba_pin:
        print('Witaj {}'.format(osoba_pin[PIN][0] + ' ' + osoba_pin[PIN][1] + '!'))
        print(' ')
        osoba = osoba_pin[PIN]
        osoba[-1] = int(osoba[-1])
        break
    elif x < 3:
        print('Masz jeszcze {} szans!'.format(3 - x))
    else:
        print('Brak dostępu! - Szanse się skończyły.')
        exit()

srodki_bankomat = [4, 6, 8, 10, 7, 3] #10, 20, 50, 100, 200, 500
suma_bankomatu = srodki_bankomat[0] * 10 + srodki_bankomat[1] * 20 + srodki_bankomat[2] * 50 + srodki_bankomat[3] * 100 + srodki_bankomat[4] * 200 + srodki_bankomat[-1] * 500

razy = [1]
his_plat = ''
transakcja_ile = [1]
def wplata(a, b, c, d, e, f):
    global suma_bankomatu
    global srodki_bankomat
    global his_plat
    global transakcja_ile
    srodki_bankomat[0] += a
    srodki_bankomat[1] += b
    srodki_bankomat[2] += c
    srodki_bankomat[3] += d
    srodki_bankomat[4] += e
    srodki_bankomat[-1] += f
    razem = a * 10 + b * 20 + c * 50 + d * 100 + e * 200 + f * 500
    suma_bankomatu += razem
    osoba[-1] = osoba[-1] + razem
    if len(transakcja_ile) == 1:
        transakcja_wplata = 'Wpłata - {} zł '.format(razem)
    if len(transakcja_ile) >= 2:
        transakcja_wplata = ', Wpłata - {} zł '.format(razem)
    transakcja_ile.append(1)
    his_plat += transakcja_wplata
    print(' ')

for x in razy:
    razy.append(1)
    print('Dane właściciela konta:')
    print('|| {} '.format(osoba[0] + ' ' + osoba[1]))
    print('|| Aktualny stan konta wynosi: {} '.format(osoba[-1]))
    if len(transakcja_ile) >= 2:
        print('|| Historia transakcji: {} '.format(his_plat))
    elif len(transakcja_ile) == 1:
        print('|| Historia transakcji: Brak ')
    odp = input('|| Jaką operację chcesz wykonać? Wypłata / Wpłata / Zakończ \n\n')
    if type(odp) == str:
        if odp.upper() == 'ZAKOŃCZ' or odp.upper() == 'ZAKONCZ':
            print(' ')
            print('Dziękujemy za użycie naszego bankomatu, zapraszamy ponownie.')
            exit()
        elif odp.upper() == 'WYPŁATA' or odp.upper() == 'WYPLATA':
            print('Wypłata')
            print(' ')
        elif odp.upper() == 'WPŁATA' or odp.upper() == 'WPLATA':
            wplata(int(input('Ilość banknotów 10zł: ')), int(input('Ilość banknotów 20zł: ')), int(input('Ilość banknotów 50zł: ')), int(input('Ilość banknotów 100zł: ')), int(input('Ilość banknotów 200zł: ')), int(input('Ilość banknotów 500zł: ')))
        else:
            print('Nie rozpoznano operacji, spróbuj ponownie.')
            print(' ')
    else:
        print('Nie rozpoznano operacji, spróbuj ponownie.')
        print(' ')

print(suma_bankomatu)
print(srodki_bankomat)