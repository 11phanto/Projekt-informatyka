global his_plat
global PIN

plik = open('dane.txt')
dane = plik.readlines()
dane = [w.split() for w in dane]

osoba_pin = {w[2]: [w[0], w[1], w[3]] for w in dane}

plik = open('transakcje.txt')
dane1 = plik.readlines()
dane1 = [w.strip('\n') for w in dane1]

for x in dane1:
    his_plat = {w[2]:dane1[dane.index(w)] for w in dane}
print(his_plat)

transakcje = {}

for x in dane1:
    transakcje = {w[2]: x for w in dane}
print(transakcje)

razy = [1]
razy_2 = [1]
for x in razy:
    print(' ')
    print('|| TRYB OPERATORA ||')
    for i in razy_2:
        srodki_bankomat = []
        ile_zlotych = [10, 20, 50, 100, 200, 500]
        czy_nie_ok = True
        for i in range(0, 6):
            czy_nie_ok = True
            while czy_nie_ok:
                odp = input('Ilość banknotów {}zł: '.format(ile_zlotych[i]))
                if odp.isdigit():
                    srodki_bankomat.append(int(odp))
                    czy_nie_ok = False
                else:
                    print(' ')
                    print('Nie podano liczby, spróbuj ponownie.')
                    print(' ')
print(' ')
suma_bankomatu = srodki_bankomat[0] * 10 + srodki_bankomat[1] * 20 + srodki_bankomat[2] * 50 + srodki_bankomat[3] * 100 + srodki_bankomat[4] * 200 + srodki_bankomat[-1] * 500

for x in range(1, 4):
    for i in range(1):
        czy_nie_ok = True
        while czy_nie_ok:
            PIN = input('Podaj PIN (x0, x0) : \n\n')
            if PIN.isdigit():
                czy_nie_ok = False
            else:
                print(' ')
                print('Nie podano liczby, spróbuj ponownie.')
                print(' ')
    if PIN in osoba_pin:
        print('Witaj {}'.format(osoba_pin[PIN][0] + ' ' + osoba_pin[PIN][1] + '!'))
        print(' ')
        osoba = osoba_pin[PIN]
        osoba.append(his_plat[PIN])
        his_plat = osoba[-1]
        osoba[2] = int(osoba[2])
        break
    elif x < 3:
        print('Masz jeszcze {} szans!'.format(3 - x))
    else:
        print('Brak dostępu! - Szanse się skończyły.')
        exit()

razy = [1]

def wyplata(a):
    global suma_bankomatu
    global srodki_bankomat
    global his_plat
    global transakcja_ile
    global test
    a = int(a)
    if a % 10 != 0:
        print('Bankomat wydaje jedynie banknoty 10zł, 20zł, 50zł, 100zł, 200zł, 500zł.')
        test = str(osoba[2])
        test = list(test)
        test[-1] = str(0)
        napis = ''
        for i in range(len(test)):
            napis = napis + i
        print('Możesz wypłacić maksymalnie: {}zł'.format(napis))
    else:
        if a > osoba[2] or suma_bankomatu < a:
            test = str(osoba[2])
            test = list(test)
            test[-1] = str(0)
            napis = ''
            for i in test:
                napis = napis + i
            if a > osoba[2] and suma_bankomatu > osoba[2]:
                print('Niewystarczająca ilość pieniędzy na koncie.')
                print('Możesz wypłacić maksymalnie {}zł'.format(napis))
            if a > suma_bankomatu and suma_bankomatu < osoba[2]:
                print('Niewystarczająca ilość pieniędzy w bankomacie.')
                print('Możesz wypłacić maksymalnie {}zł'.format(suma_bankomatu))
        elif a <= osoba[2] and suma_bankomatu >= a:
            transakcja_wyplata = ', Wyplata - {} zł '.format(a)
            osoba[-1] += transakcja_wyplata
            osoba[2] = osoba[2] - a
            ile_500 = a // 500
            a -= 500 * ile_500
            srodki_bankomat[5] = srodki_bankomat[5] - ile_500
            ile_200 = a // 200
            a -= 200 * ile_200
            srodki_bankomat[4] = srodki_bankomat[4] - ile_200
            ile_100 = a // 100
            a -= 100 * ile_100
            srodki_bankomat[3] = srodki_bankomat[3] - ile_100
            ile_50 = a // 50
            a -= 50 * ile_50
            srodki_bankomat[2] = srodki_bankomat[2] - ile_50
            ile_20 = a // 20
            a -= 20 * ile_20
            srodki_bankomat[1] = srodki_bankomat[5] - ile_20
            ile_10 = a // 10
            a -= 10 * ile_10
            srodki_bankomat[0] = srodki_bankomat[0] - ile_10
            print("Twoje pieniądze zostały wypłacone, dziękujemy za korzystanie z naszych usług!")
        print(' ')


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
    osoba[2] = osoba[2] + razem
    transakcja_wplata = ', Wpłata - {} zł '.format(razem)
    osoba[-1] += transakcja_wplata
    print(' ')

def historia_transakcji():
    print('Historia transakcji: {}'.format(osoba[-1]))

for x in razy:
    razy.append(1)
    print('Dane właściciela konta:')
    print('|| {} '.format(osoba[0] + ' ' + osoba[1]))
    print('|| Jaką operację chcesz wykonać?')
    print('|| * Stan konta')
    print('|| * Wypłata')
    print('|| * Wplata')
    print('|| * Historia tranzakcji')
    odp = input('|| * Zakończ \n \n')
    if type(odp) == str:
        if odp.upper() == 'ZAKOŃCZ' or odp.upper() == 'ZAKONCZ':
            print(' ')
            plik = open('transakcje.txt', 'w')
            print(transakcje)
            for i in transakcje:
                plik.write(transakcje[i] + '\n')
            print('Dziękujemy za użycie naszego bankomatu, zapraszamy ponownie.')
            exit()
        elif odp.upper() == 'WYPŁATA' or odp.upper() == 'WYPLATA':
            for i in range(1):
                czy_nie_ok = True
                while czy_nie_ok:
                    a = input('Podaj kwotę którą chcesz wypłacić: \n\n')
                    if a.isdigit():
                        czy_nie_ok = False
                    else:
                        print(' ')
                        print('Nie podano liczby, spróbuj ponownie.')
                        print(' ')
            wyplata(a)
        elif odp.upper() == 'WPŁATA' or odp.upper() == 'WPLATA':
            odpowiedzi = []
            ile_zlotych = [10, 20, 50, 100, 200, 500]
            czy_nie_ok = True
            for i in range(0, 6):
                czy_nie_ok = True
                while czy_nie_ok:
                    odp = input('Ilość banknotów {}zł: '.format(ile_zlotych[i]))
                    if odp.isdigit():
                        odpowiedzi.append(int(odp))
                        czy_nie_ok = False
                    else:
                        print(' ')
                        print('Nie podano liczby, spróbuj ponownie.')
                        print(' ')
            wplata(odpowiedzi[0], odpowiedzi[1], odpowiedzi[2], odpowiedzi[3], odpowiedzi[4], odpowiedzi[5])
        elif odp.upper() == 'STAN' or odp.upper() == 'STAN KONTA':
            print('Aktualny stan konta wynosi: {} '.format(osoba[2]))
            print(' ')
        elif odp.upper() == 'HISTORIA' or odp.upper() == 'HISTORIA TRANSAKCJI':
            if len(his_plat) >= 1:
                historia_transakcji()
                print(' ')
            else:
                print('Historia tranzakcji: Brak')
                print(' ')
        else:
            print('Nie rozpoznano operacji, spróbuj ponownie.')
            print(' ')
    else:
        print('Nie rozpoznano operacji, spróbuj ponownie.')
        print(' ')