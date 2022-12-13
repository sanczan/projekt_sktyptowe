#!/bin/bash

RED='\033[0;31m';
PURPLE='\033[0;35m';
ORANGE='\033[0;33m';
GREEN='\033[032m';
NC='\033[0m';

pause() {
printf "${GREEN}";
read -p "Nacisnij enter zeby kontynuowac.";
printf "${NC}";
}

menu() {
clear
printf "${ORANGE}"
echo "|^^^^  MENU  ^^^^|"
echo "|________________|"
echo "| 1 - Start      |"
echo "| 2 - Informacje |"
echo "| 3 - Backup     |"
echo "| 4 - Zakoncz    |"
echo "|________________|"
printf "${NC}";
read -n 1 -s wybor;
case $wybor in 
"1")
    wejscie="wejscie.txt"
    python3 smith.py "$wejscie"
    echo "Algorytm wykonany pomyslnie";
    pause;
    menu;
    ;;
"2")
    printf "${PURPLE}";
        echo "Algorytmion 2022 zadanie 5 - Agent Smith";
    echo "Program ma za zadanie okreslic, czy zadana liczba jest liczba smitha, czy tez nie (liczba smitha to taka liczba, ktora to jest liczba naturalnie zlozona a suma jej cyfr jest rowna sumie cyfr wszystkich swoich dzielnikow pierwszych).";
    printf "${RED}";
    echo "Autor: Slawomir Szulik.";
    printf "${NC}";
    pause;
    menu;
        ;;
"3")
    if [ ! -d "backup" ];
    then
        mkdir backup;
    fi

    printf -v date '%(%d-%m-%Y-%H:%M:%S)T\n' -1
    mkdir backup/$date

    cp ../projekt/*.txt backup/$date
    cp ../projekt/*.html backup/$date
    cp ../projekt/*.css backup/$date

    echo "Kopia pliku HTML zostala utworzona"

    printf "${RED}";
    echo "Kopia ukonczona";
    printf "${NC}";
    pause;
        menu;
        ;;
"4")
    clear;
        exit;
        ;;
*)
    echo "Nie znam polecenia";
    pause;
    menu;
esac;
};


menu
