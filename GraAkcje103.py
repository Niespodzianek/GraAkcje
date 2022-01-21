import random


def run_program():

    # Warunki początkowe

    gotowka = 10000.00
    gotowka_start = gotowka
    print(f"Początkowy stan pieniędzy to: {gotowka_start: }")
    nazwa_notowanej_spolki = random.choice(["GPW", "ORLEN", "KGHM"])
    cena_akcji_notowanej_spolki = 100.00
    liczba_posiadanych_akcji_spolki = 0
    print(f"Notowana spółka to: {nazwa_notowanej_spolki}")
    zmiennosc = 0
    srednia_cena_posiadanych_akcji = 0
    lista_wydatkow = []

    # Pętla wyboru zmienności rynku

    petla_typu_rynku = True
    while petla_typu_rynku:
        typ_rynku = input("Wybierz typ zmienności ryku: (M)Mała, (S)Średnia, (D)Duża zmienność: ")
        if typ_rynku == "M" or typ_rynku == "m":
            zmiennosc = 3
            petla_typu_rynku = False
        elif typ_rynku == "S" or typ_rynku == "s":
            zmiennosc = 10
            petla_typu_rynku = False
        elif typ_rynku == "D" or typ_rynku == "d":
            zmiennosc = 25
            petla_typu_rynku = False
        else:
            print("Zły wybór. Jeszcze raz.")

    # Główna pętla

    liczba_notowan = int(input("Podaj liczbę notowań: "))
    for licznik in range(1, liczba_notowan + 1):
        print(f"Notowanie {licznik} - cena spółki {nazwa_notowanej_spolki} = {cena_akcji_notowanej_spolki: }."
              f" Posiadasz {liczba_posiadanych_akcji_spolki} akcji spółki {nazwa_notowanej_spolki} kupionych średnio za"
              f"{srednia_cena_posiadanych_akcji: } oraz {gotowka: } pieniędzy")

        # Pętla tranzakcji

        glowna_petla_pracuje = True
        while glowna_petla_pracuje:
            decyzja = input("(K)Kupujesz, (S)Sprzedajesz akcje, (C)Czekasz do następnej sesji: ")

            # Kupowanie akcji

            if decyzja == "K" or decyzja == "k":
                petla_tranzakcji_pracuje = True
                while petla_tranzakcji_pracuje:
                    if gotowka <= 0:
                        print("Stan gotówki to 0. Nie masz pieniędzy aby kupować.")
                        petla_tranzakcji_pracuje = False
                    else:
                        print("kupujesz")
                        liczba_kupowanych_akcji = int(input(f"Podaj liczbę kupowanych akcji"
                                                            f" {nazwa_notowanej_spolki}: "))
                        if (liczba_kupowanych_akcji * cena_akcji_notowanej_spolki) > gotowka:
                            print(f"Masz za mało pieniędzy. Potrzebujesz "
                                  f"{liczba_kupowanych_akcji * cena_akcji_notowanej_spolki} a masz {gotowka}")
                            petla_tranzakcji_pracuje = False
                        else:
                            gotowka = gotowka - (liczba_kupowanych_akcji * cena_akcji_notowanej_spolki)
                            liczba_posiadanych_akcji_spolki = liczba_posiadanych_akcji_spolki + liczba_kupowanych_akcji
                            lista_wydatkow.append(liczba_kupowanych_akcji * cena_akcji_notowanej_spolki)
                            srednia_cena_posiadanych_akcji = sum(lista_wydatkow) / liczba_posiadanych_akcji_spolki
                            petla_tranzakcji_pracuje = False
                            glowna_petla_pracuje = False

            # Sprzedawanie akcji

            elif decyzja == "S" or decyzja == "s":
                petla_tranzakcji_pracuje = True
                while petla_tranzakcji_pracuje:
                    if liczba_posiadanych_akcji_spolki == 0:
                        print(f"Nie można sprzedać żadnych akcji spółki {nazwa_notowanej_spolki}"
                              f" ponieważ ich nie posiadasz.")
                        petla_tranzakcji_pracuje = False
                    else:
                        print("Sprzedajesz")
                        liczba_sprzedawanych_akcji = int(input(f"Podaj liczbę sprzedawanych akcji spółki"
                                                               f" {nazwa_notowanej_spolki}, posiadasz ich"
                                                               f" {liczba_posiadanych_akcji_spolki}: "))
                        if liczba_sprzedawanych_akcji > liczba_posiadanych_akcji_spolki:
                            print(f"Nie możesz sprzedać więcej akcji spółki {nazwa_notowanej_spolki} niż ich posiadasz"
                                  f" czyli: {liczba_posiadanych_akcji_spolki}.")
                            petla_tranzakcji_pracuje = False
                        else:
                            gotowka = gotowka + (liczba_sprzedawanych_akcji * cena_akcji_notowanej_spolki)
                            liczba_posiadanych_akcji_spolki =\
                                liczba_posiadanych_akcji_spolki - liczba_sprzedawanych_akcji
                            lista_wydatkow.append(-(liczba_sprzedawanych_akcji * cena_akcji_notowanej_spolki))
                            if liczba_posiadanych_akcji_spolki == 0:
                                srednia_cena_posiadanych_akcji = 0
                                lista_wydatkow = []
                            elif liczba_posiadanych_akcji_spolki == 0 or sum(lista_wydatkow) <= 0:
                                srednia_cena_posiadanych_akcji = 0
                                print("Ponieważ zysk ze sprzedaży części akcji przewyższył koszt inwestycji, średnia"
                                      " cena za jedną akcje wynosi 0")
                            else:
                                srednia_cena_posiadanych_akcji = sum(lista_wydatkow) / liczba_posiadanych_akcji_spolki
                            petla_tranzakcji_pracuje = False
                            glowna_petla_pracuje = False

            # Brak akcji

            elif decyzja == "C" or decyzja == "c":
                print("czekasz")
                glowna_petla_pracuje = False
            else:
                print("Zła decyzja, jeszcze raz")
        input("Naciśnij ENTER aby zakończyć aktualne notowanie")

        # Generowanie kolejnego notowania

        procent_zmiany_ceny = random.randrange(-zmiennosc, zmiennosc)
        nowa_cena_spolki = ((procent_zmiany_ceny / 100) * cena_akcji_notowanej_spolki) + cena_akcji_notowanej_spolki
        print(f"Zmiana ceny o: {procent_zmiany_ceny}% : {((procent_zmiany_ceny / 100) * cena_akcji_notowanej_spolki): .2f} : nowa cena to {nowa_cena_spolki: .2f}")
        cena_akcji_notowanej_spolki = nowa_cena_spolki

    # Koniec pracy programu-podsumowanie

    print(f"Koniec gry. Posiadasz {liczba_posiadanych_akcji_spolki} spółki {nazwa_notowanej_spolki} oraz {gotowka: }"
          f" pieniędzy")
    if liczba_posiadanych_akcji_spolki > 0:
        print("Sprzedajemy wszystkie posiadane akcje")
        gotowka = gotowka + (liczba_posiadanych_akcji_spolki * cena_akcji_notowanej_spolki)
    if gotowka > gotowka_start:
        wynik = f"zarobiono: {gotowka - gotowka_start: .2f}"
    elif gotowka < gotowka_start:
        wynik = f"stracono: {gotowka_start - gotowka: .2f}"
    else:
        wynik = "ani nie zarobiono ani nie stracono pieniędzy."
    print(f"Na początku gry posiadano {gotowka_start: }, w wyniku gry {wynik}, aktualny stan pieniędzy to:"
          f" {gotowka: .2f}")

if __name__ == "__main__":
    run_program()
    print("KONIEC PRACY PROGRAMU")

# TODO: wymyślić tytuł programu
# TODO: biblioteka matplotlib aby wyświetlać wykresy notowań i obrotów
