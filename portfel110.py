import random

class Portfel:
    def __init__(self, nazwa_portfela, sklad_portfela, gotowka=0):
        self.nazwa_portfela = nazwa_portfela
        if sklad_portfela is None:
            sklad_portfela = []
        elif len(sklad_portfela) > 100:
            sklad_portfela = sklad_portfela[:100]
        self.sklad_portfela = sklad_portfela
        self.gotowka = gotowka

    def finanse(self):
        petla_finanse = True
        while petla_finanse:
            print("\n" + "*" * 20 + "  Menu finanse  " + "*" * 20 + "\n")
            wybor_finanse = input(f"Stan gotówki: {self.gotowka}. Co wybierasz:\n(1) Wpłata\n(2) Wypłata\n")
            if wybor_finanse == "1":
                wplata = float(input("Wpisz kwotę wpłaty: "))
                self.gotowka += wplata
                print(f"Stan gotówki po wpłacie wynosi: {self.gotowka}")
                petla_finanse = False
            elif wybor_finanse == "2":
                if self.gotowka == 0:
                    print(f"Stan gotówki wynosi {self.gotowka}. Nie możesz nic wypłacić.")
                else:
                    wyplata = float(input("Wpisz kwotę wypłaty: "))
                    if wyplata > self.gotowka:
                        print(f"Nie możesz wypłacić {wyplata}. Posiadasz {self.gotowka} pieniędzy")
                    else:
                        self.gotowka -= wyplata
                        print(f"Stan gotówki po wypłacie wynosi: {self.gotowka}")
                petla_finanse = False
            else:
                print("Zły wybór !!!")
        input("Naciśnij ENTER aby przejść do głównego menu")

    def prezentacja(self):
        if len(self.sklad_portfela) == 0:
            print(f"Portfel {self.nazwa_portfela} nie zawiera żadnej pozycji ani pieniędzy {self.gotowka}")
        else:
            print(f"Portfel o nazwie - {self.nazwa_portfela} - zawiera {self.gotowka} gotówki i akcje:")
            for pozycja in self.sklad_portfela:
                # repr_pozycja = repr(pozycja)
                # print(repr_pozycja)
                print(pozycja)
                # pozycja.prezentacja()

class Akcja:
    def __init__(self, nazwa_akcji, ilosc_akcji, cena_akcji):
        self.nazwa_akcji = nazwa_akcji
        self.ilosc_akcji = ilosc_akcji
        self.cena_akcji = cena_akcji
        self.kurs_akcji = cena_akcji
        self.wartosc = self.ilosc_akcji * self.kurs_akcji

    # def prezentacja(self):
    #     print(f"Posiadasz - {self.ilosc_akcji} akcji {self.nazwa_akcji} za {self.cena_akcji} wartości {self.wartosc}")

    def __str__(self):
        return f"Posiadasz: {self.ilosc_akcji} akcji {self.nazwa_akcji} za {self.cena_akcji} wartości {self.wartosc}"

    def __repr__(self):
        return f"Posiadasz ilosc_akcji={self.ilosc_akcji} akcji spółki nazwa_akcji={self.nazwa_akcji} kupione za" \
               f" cena_akcji={self.cena_akcji} wartosc={self.wartosc}"

def tworzenie_portfela():
    lista_spolek = []
    liczba_spolek = random.randint(1, 40)
    for kolejna_spolka in range(liczba_spolek):
        nazwa = f"Spółka - {kolejna_spolka + 1}"
        ilosc = random.randint(1, 1000)
        cena = random.randint(50, 200)
        lista_spolek.append(Akcja(nazwa_akcji=nazwa, ilosc_akcji=ilosc, cena_akcji=cena))
    portfelik = Portfel(nazwa_portfela="Akcje", sklad_portfela=lista_spolek)
    print(f"Stworzono portfel złożony z {len(lista_spolek)} spółek")
    input("\nNaciśnij ENTER\n")
    return portfelik
