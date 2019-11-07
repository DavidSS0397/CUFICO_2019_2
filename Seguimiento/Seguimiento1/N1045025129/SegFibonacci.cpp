#include <iostream>
using namespace std;

int main()
{ int a, b, c;
  a = 1;
  b = 1;
  c = 0;
  
  for (int i=0; i<1000; i++)
    {
      c = a+b;
      a = b;
      b = c;
      if (c%2==0)
    {
      cout << c << endl;
    }
    }
  
return 0;
}
