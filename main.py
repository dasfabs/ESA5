import math
import random


def mensch(anzahl):
    comp = random.randrange(min, max)
    comp = int(comp)
    if (anzahl <= (max + 1) and anzahl > 1):
        comp = anzahl - 1
    if anzahl < comp:
        comp = anzahl
    anzahl = anzahl - comp
    print("Der Computer hat " + str(comp) + " gezogen")

    return anzahl


def ki(anzahl, ein):
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


def zahleingabe():
    while True:
        ein = input("Bitte eine Zahl zwischen " + str(min) + " und " + str(max) + " eingeben: ")
        ein = int(ein)
        if (ein <= max and ein >= min):
            break
    return ein


def main():
    global min, max
    min = 1
    max = 3
    anzahl = 21

    print("Streichholzspiel")
    print("Anzahl Streichhölzer: " + str(anzahl))
    print(" ")

    ki = modi()

    while anzahl > 0:

        ein = zahlEingabe()

        anzahl = anzahl - ein

        if anzahl <= 0:
            print("Ende, leider verloren")
            break

        if ki == "k":
            anzahl = ki(anzahl, ein)

        if ki == "m":
            anzahl = mensch(anzahl)

        if anzahl <= 0:
            print("Ende, du hast gewonnen")
            break

        print("Es sind noch " + str(anzahl) + " drin")


main()