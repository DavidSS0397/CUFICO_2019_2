#include <iostream>
using namespace std;
int main()
{
  int x,y,z; //Defino las variables que voy a utilizar que son numeros enteros 
  x = 0; y = 1;

  for (int i=0; i<=1000; i++)
    {
    z=(y+x);
    x=y;
    y=z;

    if ( z%2==0 )
    cout << z << endl;
    }

  return 0;

}
