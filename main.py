print ("Projekt - Miernictwo i Systemy Pomiarowe")

import csv #biblioteka obsługi plików csv
import matplotlib.pyplot as plt #biblioteka rysowania wykresów funkcji
import numpy as np #biblioteka numpy (szybkie i proste operacje na macierzach)
import time

def loadData(path):
    data = []
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            data.append(float(row[0])) #append zapamiętuje poprzednie dane dodając kolejne 1, 12, 123
    return data

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

def plot(data, periods = 4): #ile wyswietlić okresów
    T = basicPeriod(data) #wywołanie funkcji basicPeriod T-ile próbek 1 okres sygnału
    plt.plot(range(0, 3*periods*T, 3), data[:periods*T]) #zakres(od 0 do T(ile probek w okresie) * periods(ile okresów wyswietlic * 3(czas pomiedzy probkami), 3 bo próbki co 3sec)
    plt.ylabel("U [V]")
    plt.xlabel("t [s]")
    plt.show()

def printInfo(data):
    T = basicPeriod(data)*3
    print("\nNajwiększa wartość napięcia = ", max(data), " [V]")
    print("Najmniejsza wartość napięcia = ", min(data), " [V]")
    print("Okres podstawowy = ", T, " [s]")
    print("Częstotliwość = ", 1/T, " [Hz]")
    print("Wartosc skuteczna = ", effectiveValue(data), " [V] \n")

def menu():
    print("[1] Wczytaj plik: 'u_swietlowka_12W.csv'")
    print("[2] Wczytaj plik: 'u_LED_2W.csv'")
    print("[3] Wyświetl wykres")
    print("[4] Wyświetl parametry")
    print("[0] Koniec Programu")
    ch = int(input("Wybierz swoją opcje: ")) #wybór działania przez użytkownika
    return ch #zapamiętuje zadany prze użytkownika numer

dane = None
while True: #pętla która wykonuje sie w nieskończoność dopóki "break"
    choice = menu()
    if choice == 0:
        print(" \n Dziękuje za użytkowanie programu. Z wyrazami szacunku \n Dawid Mądry \n Energetyka EN-2 \n Semestr 3 \n 144973")
        time.sleep(3)
        break

    elif choice == 1:
        print("\nProgram wczytuje dane \n")
        dane = loadData('u_swietlowka_12W.csv')
        print("Dane zostały wczytane \n")

    elif choice == 2:
        print("\nProgram wczytuje dane \n")
        dane = loadData('u_LED_2W.csv')
        print("Dane zostały wczytane \n")

    elif choice == 3:
        if dane == None:
            print("Nie wczytano pliku. Wybierz [1] lub [2] przed wyświetleniem wykresu")
        else:
            plot(dane)

    elif choice == 4:
        if dane == None:
            print("Nie wczytano pliku. Wybierz [1] lub [2] przed wyświetleniem parametrów")
        else:
            printInfo(dane)

    else:
        print("Nieprawidłowy numer")

    time.sleep(1)