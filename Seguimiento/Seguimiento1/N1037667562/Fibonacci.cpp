/*
Programa que calcula los numeros de Fibonacci
Imprime solo los pares
*/

#include <iostream>
using namespace std;

int main()
{
  long int f0,f1,c;
  f0=0; f1=1; c=0;

  for (int i=0; i<1000; i++)
    {
      c=f0+f1; f0=f1; f1=c;
      if ( c%2 == 0)
	{
	  cout << c << endl;
	}
    }

  return 0;
}
