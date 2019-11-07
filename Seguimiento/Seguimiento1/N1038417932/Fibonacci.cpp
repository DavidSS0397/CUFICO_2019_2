/*
Este es un script en c++ que calcula los primeros 1000 digitos de la serie de fibonacci  e imprime los pares
*/ 

#include <iostream>
using namespace std;

int main()
{
  int Fib_2=0;
  int Fib_1=1;
  cout <<  Fib_2 << endl;

  int Fib;
  int val;
  
  for (int i=2; i<1000;i++ )
    {

      Fib= Fib_2 + Fib_1 ;
    val= Fib%2 ;
    if ( val == 0 )
      {
	cout<< Fib <<endl;
      }

    Fib_2=Fib_1;
      Fib_1=Fib;
      }

return 0;
}
