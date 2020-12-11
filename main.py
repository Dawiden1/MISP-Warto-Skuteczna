print ("Projekt - Miernictwo i Systemy Pomiarowe")

import csv #biblioteka obsługi plików csv
import matplotlib.pyplot as plt #biblioteka rysowania wykresów funkcji
import numpy as np #biblioteka numpy (szybkie i proste operacje na macierzach)
import time

def loadData(path = None):
    if path == None:
        path = input("Podaj ścieżkę: ")
    data = []
    try:
        print("\nProgram wczytuje dane \n")
        with open(path) as csvfile:
            readCSV = csv.reader(csvfile)
            for row in readCSV:
                data.append(float(row[0])) #append zapamiętuje poprzednie dane dodając kolejne 1, 12, 123
        print("Dane zostały wczytane \n")
        sampling = int(input("Podaj częstotliwość próbkowania: "))
        return data, sampling
    except:
        print("Nie udało się wczytać pliku. Upewnij się, że plik pod wybraną ścieżką istnieje")
        return None

def basicPeriod(data):
    zeros = []
    for i in range(len(data) - 1):
        if data[i] * data[i + 1] < 0:
            zeros.append(i)
        if len(zeros) > 2:
            break
    return zeros[2] - zeros[0]

def effectiveValue(data):
    T = basicPeriod(data)
    eV = 0
    for i in range(T):
        eV += data[i]**2
    return (eV/T)**(1/2)

def plot(data, sf, periods = 4): #periods oznacza ile wyswietlić okresów
    T = basicPeriod(data) #wywołanie funkcji basicPeriod T-ile próbek 1 okres sygnału
    plt.plot(np.arange(0, periods*T/sf, 1/sf), data[:periods*T]) #zakres(od 0 do T(ile probek w okresie) * periods(ile okresów wyswietlic * 3(czas pomiedzy probkami), 3 bo próbki co 3sec)
    plt.ylabel("U [V]")
    plt.xlabel("t [s]")
    plt.show()

def printInfo(data, sf):
    T = basicPeriod(data)/sf

    """
    Praca nad nowymi parametrami ws
    
    """
    print("\nNajwiększa wartość napięcia = ", max(data), " [V]")
    print("Najmniejsza wartość napięcia = ", min(data), " [V]")
    print("Okres podstawowy = ", T, " [s]")
    print("Częstotliwość = ", 1/T, " [Hz]")
    print("Wartosc skuteczna = ", effectiveValue(data), " [V] \n")

def menu():
    print("\n[1] Wczytaj plik: 'u_swietlowka_12W.csv'")
    print("[2] Wczytaj plik: 'u_LED_2W.csv'")
    print("[3] Wczytaj plik z wybranej ścieżki")
    print("[4] Wyświetl wykres")
    print("[5] Wyświetl parametry")
    print("[0] Koniec Programu")
    ch = int(input("Wybierz swoją opcje: ")) #wybór działania przez użytkownika
    return ch #zapamiętuje zadany prze użytkownika numer

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
            print("Nie wczytano pliku. Wybierz [1] lub [2] przed wyświetleniem wykresu")
        else:
            plot(dane, sampling_frequency)

    elif choice == 5:
        if dane == None:
            print("Nie wczytano pliku. Wybierz [1] lub [2] przed wyświetleniem parametrów")
        else:
            printInfo(dane, sampling_frequency)

    else:
        print("Nieprawidłowy numer")

    time.sleep(1)