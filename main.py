def ki(anzahl,ein):

    if ein == 1:
        comp = 3
    elif ein == 2:
        comp = 2
    else:
        comp = 1
    print("Der Computer hat " + str(comp) + " gezogen")
    anzahl = anzahl - comp
    return anzahl


def modi():
    while True:
        ki = input("Mensch (m) oder KI (k) als Gegner: ")
        if (ki == "m" or ki == "k"):
            break
    return ki

def main():
    global min,max
    min = 1
    max = 3
    anzahl = 21

    print("Streichholzspiel")
    print("Anzahl Streichhölzer: "+ str(anzahl))
    print(" ")