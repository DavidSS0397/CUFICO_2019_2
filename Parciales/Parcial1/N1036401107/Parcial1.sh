#!/bin/bash                                                                                                                                    

echo "Ingrese n tal que 1=Código de C++ y 2= Código de python"
read n
if [ $n == 1 ]
then
    g++ -o Problema1 Problema1.cpp && ./Problema1

elif [ $n == 2 ]
then
    python Problema2.py
fi
