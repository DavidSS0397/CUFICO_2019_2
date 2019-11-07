#include <iostream>
using namespace std;

int main()
{
  int x;
  int y;
  x=0;
  y=1;
  int s;
  for (int i=0; i<=1000; i++)
    {
     
      s=y+x;
      x=y;
      y=s;

      if (s%2==0)
	{
	  cout << "fibo par:" << " " << s  << endl;
	}
    }
  return 0;
}
