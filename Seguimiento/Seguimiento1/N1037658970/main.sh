#!/bin/sh
#Programa que ejecuta RK6 de C++, guarda los resultados en dat.txt y ejecuta un .py para graficar


g++ -o RK6 RK6.cpp
./RK6 >> dat.txt
python3 RK6.py