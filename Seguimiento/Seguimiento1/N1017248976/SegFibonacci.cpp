#include <iostream> /*Import iostream=in or out stream */
using namespace std;//sirve para quitar todos los std
int main()
{
  int x=1;
  int y=1;
  int Z=0;
  for (int i=0;i<100;i++)
    {
      Z=x+y;
      x=y;
      y=Z;
      if( Z%2 == 0 )
	{
	  cout << Z << endl;
	}
    }
return 0;
}
