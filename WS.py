print ("Projekt - Miernictwo i Systemy Pomiarowe \n Dawid Mądry \n Energetyka EN-2 \n Semestr 3 \n 144973")

import csv
import matplotlib.pyplot as plt

# dane
dane = []
N = 500 # liczba próbek
T = 3*N # czas trwania pomiaru


#wczytywanie N pierwszych próbek do "dane"
i = 0
with open('u_LED_2W.csv') as csvfile:
    readCSV = csv.reader(csvfile)

    for row in readCSV:
        i += 1
        if i>N:
            break
        dane.append(float(row[0]))

#obliczanie całki z próbek
calka = 0
for x in dane:
    calka += (x**2)*3


#obliczanie wartości skutecznej z całki
Usk = (calka/T)**(1/2)


#wyświetlanie
print(Usk)

plt.plot(dane)
plt.show()