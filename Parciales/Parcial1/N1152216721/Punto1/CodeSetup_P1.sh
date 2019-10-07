#!/bin/bash
echo Compilación y ejecución del Punto 1 del Parcial.
echo El código está escrito en primera instancia para reconocer 
echo ingresos por teclado que no correspondan a lo solicitado.

g++ -Wall -Werror -Wextra -o Problema1.exe Problema1.cpp

./Problema1.exe

echo "*************************************************************"
echo "CONCLUSIÓN DE LAS PRUEBAS HECHAS PRE-ENTREGA:"
echo Según la mayoría de ejecuciones, se puede concluir que con
echo las condiciones de supervivencia dadas, la especie 1 parece 
echo ser dominante respecto a la especie 2.
echo "*************************************************************"
