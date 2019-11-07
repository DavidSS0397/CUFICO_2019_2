


#include <iostream>
#include <cmath>


using namespace std;

int main()

{

	double Fi=0;
	double Ff=1;
	double i=1;


	while (i<100)
	{
		 double Fn = Fi + Ff;

		Fi=Ff;
		Ff=Fn;

		if (fmod(Fn,2) == 0)
		{
			cout << Fn << endl;
			i=i+1;
		}
		
		Fn=0;	
	}

return 0;

}

