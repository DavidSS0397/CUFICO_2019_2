#include <iostream>

using namespace std;


int main()
{
  int f0=0;
  int f1=0;
  int f=1;

  for (int i; i<100; i++)
    {



      f+=f0;
	f0=f1;
	f1=f;
	//		cout << f << endl;
	if(  ( f % 2) == 0)
	  {
	    cout << f <<endl;
	  }
	}



  return 0;
}
