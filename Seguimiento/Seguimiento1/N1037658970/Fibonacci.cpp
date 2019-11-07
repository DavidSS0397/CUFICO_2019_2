/*
! Fibonacci.cpp
! Programa que calcula los primero 1000 numeros de la serie de Fibonacci
! e imprime en pantalla los pares.
! Last Update: 28 agosto 2019
! @uthor: Valentina Roquemen
*/

#include <iostream>
using namespace std;

int main()
  {
    int fn2,fn1,fn;
    fn1 = 1; fn2=0;

    for (int i=0;i<1000;i++)
      {
	fn = fn1+fn2;
	
	if ( fn%2 == 0)
	  {
	    cout << fn << endl;
	  }
	fn2 = fn1;
	fn1 = fn;
      }
    return 0;
  }
