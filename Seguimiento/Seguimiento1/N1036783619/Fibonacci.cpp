#include <iostream>
using namespace std;
int main ()
{
  int f0 = 0; //Define los primeros pasos de recurrencia
  int f1 = 1;
  for (int i=0; i<1000; i++)
      {
	int f2 = f1 + f0; // Define el siguiente término
	if (f2%2==0) // Condición para los pares
       {
	 cout << f2 << "" << endl;
		   
       }
       else
       {
	 
       }
	f0 = f1; //Se aplica recurrencia
       f1 = f2;
      }  
  return 0;
}

