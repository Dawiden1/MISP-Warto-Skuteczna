print ("Projekt - Miernictwo i Systemy Pomiarowe")

import csv #biblioteka obsługi plików csv
import matplotlib.pyplot as plt #biblioteka rysowania wykresów funkcjiddd

# dane
dane = [] #tabela z danymi
N = 1800 # liczba próbek
T = 3*N # czas trwania pomiaru


#wczytywanie N pierwszych próbek do "dane"
i = 0
with open('u_swietlowka_12W.csv') as csvfile:
    readCSV = csv.reader(csvfile)

    for row in readCSV: #zapętlanie wierszowo pliku csv
        i += 1
        if i>N:
            break
        dane.append(float(row[0])) #zamiana liczb calkowitych w tabeli na liczby zmiennoprzecinkowe

def menu():
    print("[1] Wartosc Skuteczna Napięcia")
    print("[2] Opcja 2")

def Wartosc_Skuteczna():
    #obliczanie całki z próbek
        calka = 0
        for x in dane:
            calka += (x**2)*3

    #obliczanie wartości skutecznej z całki
        Usk = (calka/T)**(1/2)

    #wyświetlanie
        print("Wartość Skuteczna Napięcia = ", end='')
        print(Usk)

        plt.plot(dane) #tworzeniew wykresu
        plt.show() #wyświetlenie wykresu

        print("Największa wartość napięcia =", max(dane))
        print("Najmniejsza wartość napięcia =", min(dane))

menu()
opcje = int(input("Wybierz swoją opcje: "))

while opcje != 0:
    if opcje == 1:
        print("Wybrałeś Wartość Skuteczną")
        Wartosc_Skuteczna()

    elif opcje == 2:
        print("Tu jeszcze nic nie ma")

        #program

    else:
        print("Nieprawidłowy numer")

    menu()
    opcje = int(input("Wybierz swoją opcje: "))

print("Dziękuje za użytkowanie programu. Z wyrazami szacunku \n Dawid Mądry \n Energetyka EN-2 \n Semestr 3 \n 144973")





print("Koniec Programu")



""" Stary kod

print ("Projekt - Miernictwo i Systemy Pomiarowe \n Dawid Mądry \n Energetyka EN-2 \n Semestr 3 \n 144973")

import csv #biblioteka obsługi plików csv
import matplotlib.pyplot as plt #biblioteka rysowania wykresów funkcji

# dane
dane = [] #tabela z danymi
N = 1000 # liczba próbek
T = 3*N # czas trwania pomiaru


#wczytywanie N pierwszych próbek do "dane"
i = 0
with open('u_LED_2W.csv') as csvfile:
    readCSV = csv.reader(csvfile)

    for row in readCSV: #zapętlanie wierszowo pliku csv
        i += 1
        if i>N:
            break
        dane.append(float(row[0])) #zamiana liczb calkowitych w tabeli na liczby zmiennoprzecinkowe

odpowiedz = None
while odpowiedz not in ("Nie", "nie"):
    odpowiedz = input("Chcesz zobaczyć wykres i wartość skuteczna napięcia?: " )
    if odpowiedz == "tak" or odpowiedz == "Tak":

#obliczanie całki z próbek
        calka = 0
        for x in dane:
            calka += (x**2)*3

#obliczanie wartości skutecznej z całki
        Usk = (calka/T)**(1/2)

#wyświetlanie
        print("Wartość Skuteczna Napięcia = ", end='')
        print(Usk)

        plt.plot(dane) #tworzeniew wykresu
        plt.show() #wyświetlenie wykresu

        print("Największa wartość napięcia =", max(dane))
        print("Najmniejsza wartość napięcia =", min(dane))

print("Koniec Programu")


"""