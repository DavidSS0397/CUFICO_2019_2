#!/bin/bash
echo "Buenos días Jotadram6"
echo "Indique que código quiere correr"
echo "1: Juego de la vida"
echo "2: Sistema de dos gases"
read n
if [ $n == 1 ]
then
echo "sugerencia: Las condiciones iniclaes por defecto de la matriz implican  que sea minimo de 5x5, pero si la pone de menos tampoco hay problema."
g++ -o Parcial1P1 Parcial1P1.cpp && ./Parcial1P1

elif [ $n == 2 ]
then
    echo "Este se demora un poco más"
    python3 Parcial1P2.py

else
    echo "Porfavor ingrese una opción válida (1 o 2)"
    
fi
