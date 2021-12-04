
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

    ki = modi()