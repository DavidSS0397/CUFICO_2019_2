#include <iostream>
using namespace std;
int f0=0;
int f1=1;
int fn=0;

int main()
{ 
  for (int i=0; i<1000; i++)
    { fn=f0+f1;
      f0=f1;
      f1=fn;
      //cout << fn << endl;
      if ( fn%2 == 0)
	{ cout << fn << endl;
	}
      
    }
  return 0;

}
