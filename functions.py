import csv  # biblioteka obsługi plików csv
import matplotlib.pyplot as plt  # biblioteka rysowania wykresów funkcji
import numpy as np  # biblioteka numpy (szybkie i proste operacje na macierzach)


def loadData(path=None):
    if path == None:
        path = input("Podaj ścieżkę: ")
    data = []
    try:
        print("\nProgram wczytuje dane \n")
        with open(path) as csvfile:
            readCSV = csv.reader(csvfile)
            for row in readCSV:
                data.append(float(row[0]))  # append zapamiętuje poprzednie dane dodając kolejne 1, 12, 123
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


def effectiveValue(data, start, stop):
    start = int(start)
    stop = int(stop)
    eV = 0
    for i in range(start, stop):
        eV += data[i] ** 2
    return (eV / (stop - start)) ** (1 / 2)


def plot(data, sf, to_show):  # periods oznacza ile wyswietlić okresów
    plt.plot(np.arange(0, to_show / sf, 1 / sf), data[:to_show])  # zakres(od 0 do T(ile probek w okresie) * periods(ile okresów wyswietlic * 3(czas pomiedzy probkami), 3 bo próbki co 3sec)
    plt.ylabel("U [V]")
    plt.xlabel("t [s]")
    plt.show()


def printInfo(data, sf):
    T = basicPeriod(data)

    time = float(input("Podaj okno czasowe w sekundach, w którym zostanie obliczona wartość skuteczna: "))
    sample_n = int(sf * time)
    sample_n = min(sample_n, len(data))

    half_periods = int(2 * sample_n / T)

    eV = []
    for x in range(half_periods - 1):
        eV.append(effectiveValue(data, x * T / 2, (x + 2) * T / 2))

    with open("Wygenerowane wartości skuteczne", "w") as output:
        for row in eV:
            output.write(str(row) + " [V] \n")

    print("\nŚrednia zagregowana wartosci skutecznej = ", np.mean(eV), " [V] ")
    print("Największa wartość napięcia = ", max(data), " [V]")
    print("Najmniejsza wartość napięcia = ", min(data), " [V]")
    print("Okres podstawowy = ", T / sf, " [s]")
    print("Częstotliwość = ", sf / T, " [Hz]\n")

    print("\nWartości skuteczne poszczególnych okresów zostały eksportowane do pliki .txt w głównym folderze z aplikacją ")

    plot(data, sf, sample_n)


def menu():
    print("\n[1] Wczytaj plik: 'u_swietlowka_12W.csv'")
    print("[2] Wczytaj plik: 'u_LED_2W.csv'")
    print("[3] Wczytaj plik z wybranej ścieżki")
    print("[4] Wyświetl informacje")
    print("[0] Koniec Programu")
    try:
        ch = int(input("Wybierz swoją opcje: "))  # wybór działania przez użytkownika
    except:
        ch = -1
    return ch  # zapamiętuje zadany prze użytkownika numer