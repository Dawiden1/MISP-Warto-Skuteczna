print ("Projekt - Miernictwo i Systemy Pomiarowe")

from functions import *

dane = None
sampling_frequency = None

while True: #pętla która wykonuje sie w nieskończoność dopóki "break"
    choice = menu()
    if choice == 0:
        print(" \n Dziękuje za użytkowanie programu. Z wyrazami szacunku \n Dawid Mądry \n Energetyka EN-2 \n Semestr 3 \n 144973")
        time.sleep(3)
        break

    elif choice in [1, 2, 3]:
        X = ['u_swietlowka_12W.csv', 'u_LED_2W.csv', None]
        dane, sampling_frequency = loadData(X[choice - 1])

    elif choice == 4:
        if dane == None:
            print("Nie wczytano pliku. Wybierz [1], [2] lub [3]")
        printInfo(dane, sampling_frequency)

    else:
        print("Nieprawidłowy numer")
