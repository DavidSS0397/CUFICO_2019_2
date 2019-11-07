#include <iostream>
using namespace std;

int main()
{
  int f0 = 0;  
  int f1 = 1;
  
  for (int i=0; i<1000; i++)
   {
    int f2 = f0 + f1;
    
    if (f2% == 0)
     {
      cout << f2 << endl;
     }
    f0 = f1;
    f1 = f2;
   }
  return 0;
}
  
