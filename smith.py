import sys
import os
from datetime import date, datetime
from os.path import isfile, join, exists

def sum_f(number):  # zlicza sumę cyfr podanej liczby
    suma = 0
    for element in number:
        suma += int(element)
    return str(suma)


def divider(number):  # zwraca łańcuch znaków dzielników prostych podanej liczby
    num = int(number)
    s = ""
    for n in range(2, int(number) + 1):
        for j in range(2, int(number)):
            if num % j == 0:
                s += str(j)
                num /= j
                break
    return s


def is_smith(numba):  # główna funkcja sprawdzająca, czy liczba jest liczbą Smith'a
    num = str(numba)
    suma = sum_f(num)
    div = sum_f(divider(num))

    if suma == div and numba != '0':
        return True
    else:
        return False


if __name__ == '__main__':  # ciało główne programu
    wejscie = sys.argv[1]
    zapisz = open("wyjscie.txt", "w")
    zapisz.seek(0)  # <- This is the missing piece
    zapisz.truncate()
    with open(wejscie, "r") as file:  #odczytanie z pliku linijka po linijce
        lines = [line.rstrip() for line in file]

        for i in lines:
            if i.isdigit(): #jezeli linia jest cyfra to sprawdza czy smith
                if is_smith(i):  # wypisanie uzytkownikowi, czy zadana przez niego liczba, jest liczba Smith'a
                    #print("Liczba ta jest liczbą Smith'a")
                    zapisz.write("Liczba Smith'a\n")
                else:
                    #print("Liczba ta nie jest liczbą Smith'a")
                    zapisz.write("Zwykla liczba\n")
            else:
                #print(i)
                zapisz.write("Nie jest to liczba\n")
    zapisz.close()

    if exists("raport.html"):
        os.remove("raport.html")
    now = datetime.now()
    fulldate = now.strftime("%d-%m-%Y %H:%M:%S")

    wyjscie = open("raport.html", "a+")

    wyjscie.write(f"""

    <html>
      <head>
        <title>Raport</title>
        <link rel="stylesheet" href="style.css">
      </head>
      <body>
      <h1>Raport z dnia: {fulldate}</h1>
      <table>
        <tr>
          <th>input</th>
          <th>output</th>
        </tr>
        """)
    wyjscie.write(""" <tr>""")

    with open(wejscie, "r") as f1, open("wyjscie.txt", "r") as f2:  #odczytanie z pliku linijka po linijce
        linia1 = [line.rstrip() for line in f1]
        linia2 = [line.rstrip() for line in f2]

        for i,j in zip(linia1, linia2):
            wyjscie.write("<td>")

            wyjscie.write(str(i))

            wyjscie.write("""</td><td>""")

            wyjscie.write(str(j))

            wyjscie.write("""</td>
            </tr>""")

    wyjscie.write("""
      </table>
      </body>
    </html>""")

    wyjscie.close()

