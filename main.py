from gra import gra_gieldowa as gra

def przeglad_portfela():
    print("Przegląd portfela")

def finanse():
    print("Finanse")

def menu():
    petla_menu = True
    while petla_menu:
        print("\n" + 20 * "*" + "MENU GŁÓWNE PROGRAMU" + 20 * "*" + "\n")
        wybor_menu = input("(P)Przegląd portfela\n(F)Finanse - wpłata / wypłata\n(G)Gra giełdowa\n(Q)Koniec pracy programu\n\n")
        if wybor_menu == "P" or wybor_menu == "p":
            przeglad_portfela()
        elif wybor_menu == "F" or wybor_menu == "f":
            finanse()
        elif wybor_menu == "G" or wybor_menu == "g":
            gra()
        elif wybor_menu == "Q" or wybor_menu == "q":
            petla_menu = False
        else:
            print("Zły wybór")

if __name__ == '__main__':
    menu()
    print("KONIEC PRACY PROGRAMU")
