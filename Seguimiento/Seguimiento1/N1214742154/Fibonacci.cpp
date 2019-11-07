//Fibonnaci in c++ by Juan David Tobon
#include <iostream>
using namespace std;

int main()
{
  int f_n_minus_2 = 0;
  int f_n_minus_1 = 1;

  cout << f_n_minus_2 << endl;

  int f_n;
  int val;
  
  for (int i = 2; i <1000 ; i++)
    {

      f_n = f_n_minus_2 + f_n_minus_1;
      val = f_n%2;
	if ( val == 0 )
	  {
	    cout << f_n << endl;
	  }

      f_n_minus_2 = f_n_minus_1;
      f_n_minus_1 = f_n;

    }
  
  return 0;
}
