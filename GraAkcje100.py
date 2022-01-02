import random


def run_program():
    gotowka = 10000
    gotowka_start = gotowka
    print(f"Początkowy stan pieniędzy to: {gotowka_start: .2f}")
    nazwa_notowanej_spolki = random.choice(["GPW", "ORLEN", "KGHM"])
    cena_akcji_notowanej_spolki = 100
    liczba_posiadanych_akcji_spolki = 0
    print(f"Notowana spółka to: {nazwa_notowanej_spolki}")
    liczba_notowan = int(input("Podaj liczbę notowań: "))

    # Główna pętla programu

    for licznik in range(1, liczba_notowan + 1):
        print(f"Notowanie {licznik} - cena spółki {nazwa_notowanej_spolki} = {cena_akcji_notowanej_spolki: .2f}."
              f" Posiadasz"
              f" {liczba_posiadanych_akcji_spolki} akcji i {gotowka: .2f} pieniędzy")
        czy_glowna_petla_pracuje = True
        while czy_glowna_petla_pracuje:

            # Kupowanie akcji

            decyzja = input("(K)Kupujesz, (S)Sprzedajesz akcje, (C)Czekasz do następnej sesji: ")
            if decyzja == "K" or decyzja == "k":
                czy_petla_tranzakcji_pracuje = True
                while czy_petla_tranzakcji_pracuje:
                    print("kupujesz")
                    liczba_kupowanych_akcji = int(input(f"Podaj liczbę kupowanych akcji {nazwa_notowanej_spolki}: "))
                    if (liczba_kupowanych_akcji * cena_akcji_notowanej_spolki) > gotowka:
                        print(f"Masz za mało pieniędzy. Potrzebujesz "
                              f"{liczba_kupowanych_akcji * cena_akcji_notowanej_spolki} a masz {gotowka}")
                        czy_petla_tranzakcji_pracuje = False
                        czy_glowna_petla_pracuje = True
                    else:
                        gotowka = gotowka - (liczba_kupowanych_akcji * cena_akcji_notowanej_spolki)
                        liczba_posiadanych_akcji_spolki = liczba_posiadanych_akcji_spolki + liczba_kupowanych_akcji
                        czy_petla_tranzakcji_pracuje = False
                        czy_glowna_petla_pracuje = False

                # Sprzedawanie akcji

            elif decyzja == "S" or decyzja == "s":
                czy_petla_tranzakcji_pracuje = True
                while czy_petla_tranzakcji_pracuje:
                    print("Sprzedajesz")
                    liczba_sprzedawanych_akcji = int(input(f"Podaj liczbę sprzedawanych akcji spółki "
                                                           f"{nazwa_notowanej_spolki}, posiadasz ich"
                                                           f" {liczba_posiadanych_akcji_spolki}: "))
                    if liczba_posiadanych_akcji_spolki == 0:
                        print(f"Nie można sprzedać żadnych akcji spółki {nazwa_notowanej_spolki}"
                              f" ponieważ ich nie posiadasz.")
                        czy_petla_tranzakcji_pracuje = False
                        czy_glowna_petla_pracuje = True
                    elif liczba_sprzedawanych_akcji > liczba_posiadanych_akcji_spolki:
                        print(f"Nie możesz sprzedać więcej akcji spółki {nazwa_notowanej_spolki} niż ich posiadasz"
                              f" czyli: {liczba_posiadanych_akcji_spolki}.")
                        czy_petla_tranzakcji_pracuje = False
                        czy_glowna_petla_pracuje = True
                    else:
                        gotowka = gotowka + (liczba_sprzedawanych_akcji * cena_akcji_notowanej_spolki)
                        liczba_posiadanych_akcji_spolki = liczba_posiadanych_akcji_spolki - liczba_sprzedawanych_akcji
                        czy_petla_tranzakcji_pracuje = False
                        czy_glowna_petla_pracuje = False
            elif decyzja == "C" or decyzja == "c":
                print("czekasz")
                czy_glowna_petla_pracuje = False
            else:
                print("Zła decyzja, jeszcze raz")
        input("Naciśnij ENTER aby zakończyć aktualne notowanie")

        # Generowanie kolejnego notowania

        procent_zmiany_ceny = random.randrange(-10, 10)
        wartosc_zmiany = ((procent_zmiany_ceny / 100) * cena_akcji_notowanej_spolki)
        nowa_cena_spolki = ((procent_zmiany_ceny / 100) * cena_akcji_notowanej_spolki) + cena_akcji_notowanej_spolki
        print(f"Zmiana ceny o: {procent_zmiany_ceny}% : {wartosc_zmiany: .2f} : nowa cena to {nowa_cena_spolki: .2f}")
        cena_akcji_notowanej_spolki = nowa_cena_spolki
    print(f"Koniec gry. Posiadasz {liczba_posiadanych_akcji_spolki} spółki {nazwa_notowanej_spolki} oraz {gotowka: .2f}"
          f" pieniędzy")

    # Koniec pracy programu-podsumowanie

    if liczba_posiadanych_akcji_spolki > 0:
        print("Sprzedajemy wszystkie posiadane akcje")
        gotowka = gotowka + (liczba_posiadanych_akcji_spolki * cena_akcji_notowanej_spolki)
    if gotowka > gotowka_start:
        wynik = f"zarobiono: {gotowka - gotowka_start: .2f}"
    elif gotowka < gotowka_start:
        wynik = f"stracono: {gotowka_start - gotowka: .2f}"
    else:
        wynik = "ani nie zarobiono ani nie stracono pieniędzy."
    print(f"Na początku gry posiadano {gotowka_start: .2f}, w wyniku gry {wynik}, aktualny stan pieniędzy to:"
          f" {gotowka: .2f}")

if __name__ == "__main__":
    run_program()
    print("KONIEC PRACY PROGRAMU")
