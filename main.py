import personbil
import lastbil

looping = True

#initierar objekt av klasser
opel_gron=personbil.Personbil("opel", "gron", 1)
BMW_vit=personbil.Personbil("BMW", "vit", 2)

Scania_rosa = lastbil.lastbil("scania", "rosa", 5000)
Volvo_Rost = lastbil.lastbil("volvo","rost", 1)

Personbils_lista = [opel_gron, BMW_vit]
Lastbils_lista = [Scania_rosa, Volvo_Rost]

def print_fordonslista(fordonslista):
    for ettfordon in fordonslista:
        ettfordon.print_fordon()

while looping:

    print("------------------------------------------------------------")
    print("\n klasser och arv av fordon \n")

    val_fordon = input("Vilken fordonstyp vill du lista? 1=lastbil 2=personbil: ")

    if (val_fordon == "1"):
        print("\n-lastbilar-")
        print("--------------------------------------------------------")
        print_fordonslista(Lastbils_lista)

    elif (val_fordon == "2"):
        print("\n-personbilar-")
        print("--------------------------------------------------------")
        print_fordonslista(Personbils_lista)

    else:
        print("\nOgiltig inmatning! \n")
    
    go = input("\n Vill ni lista fordonen igen? j/n ")

    if (go == "n"):
        break