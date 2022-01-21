from gra import gra_gieldowa as gra
from portfel import tworzenie_portfela


def menu():
    portfel = None
    petla_menu = True
    while petla_menu:
        print("\n" + 20 * "*" + "  MENU GŁÓWNE PROGRAMU  " + 20 * "*" + "\n")
        wybor_menu = input("(T)Tworzenie nowego portfela\n"
                           "(O)Otwieranie portfela z pliku\n"
                           "(P)Przegląd portfela\n"
                           "(F)Finanse - wpłata / wypłata\n"
                           "(G)Gra giełdowa\n"
                           "(Q)Koniec pracy programu\n\n")
        if wybor_menu == "T" or wybor_menu == "t":
            portfel = tworzenie_portfela()
        elif wybor_menu == "O" or wybor_menu == "o":
            print("Otwieranie pliku z dysku")
        elif wybor_menu == "P" or wybor_menu == "p":
            if portfel is None:
                print("Nie stworzono jeszcze żadnego portfela")
            else:
                portfel.prezentacja()
        elif wybor_menu == "F" or wybor_menu == "f":
            if portfel is None:
                print("Nie stworzono jeszcze żadnego portfela. Przed wpłatą lub wypłatą trzeba utworzyć portfel.")
            else:
                portfel.finanse()
        elif wybor_menu == "G" or wybor_menu == "g":
            gra()
        elif wybor_menu == "Q" or wybor_menu == "q":
            petla_menu = False
        else:
            print("Zły wybór !!!")

if __name__ == '__main__':
    menu()
    print("KONIEC PRACY PROGRAMU")
