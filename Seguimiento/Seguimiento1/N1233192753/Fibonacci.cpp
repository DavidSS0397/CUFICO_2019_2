#include <iostream>
using namespace std;

int main()
{
  int f0 = 0;
  int f1 = 1;     //Definicion de variables 

  for ( int i = 1; i <=1000; i++)
    {
      int fn;
      fn = f0 + f1;     // calculo termino n 




      if ( fn % 2 == 0)       // condicion de par 
        {
          cout << fn << endl;   
        }

      f0 = f1;  // redefinicion de variables 
      f1 = fn;
    }

  return 0;
}


