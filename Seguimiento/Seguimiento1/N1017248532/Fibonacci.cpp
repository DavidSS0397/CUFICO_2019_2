#include <iostream>
using namespace std;

int main()
{
  int a,b,c;
  a=1; b=0;
  
  for(int i=0; i<1000; i++)
    {
      c = a+b;

      if (c%2 == 0)
	{
	  cout << c << endl;
	}
      b = a;
      a = c;
    }
  return 0;
}
