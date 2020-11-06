print ("Projekt - Miernictwo i Systemy Pomiarowe \n Dawid Mądry \n Energetyka EN-2 \n Semestr 3 \n 144973")


import csv
with open('u_LED_2W.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        print(row)