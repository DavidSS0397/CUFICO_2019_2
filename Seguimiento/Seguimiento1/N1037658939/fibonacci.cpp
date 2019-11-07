#include <iostream>
using namespace std;

int main()
{
	int n = 0, mod = 0;
	long f0 = 0, f1 = 1, fn = 0;

	for (n=1; n<=1000; n++)
	{
		fn = f0 + f1;
		mod = fn%2;

		if (mod == 0) cout << fn << endl;

		f0 = f1;
		f1 = fn;
	}

	return 0;
}
