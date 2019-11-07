/* 
Este código contiene el método de RK6 
*/

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

//Definimos la funcion del método RK6
float RK6(float xn, float yn, float h, float (*MyF)(float, float))
{
	float k1, k2, k3 ,k4, k5 , k6;
	k1 = MyF(xn, yn);
	k2 = MyF(xn+h/3, yn+h*k1/3);
	k3 = MyF(xn+h*3/4, yn+h*(123*k1/256 + 315*k2/256));
	k4 = MyF(xn+h/5, yn+h*(193*k1/750 + 189*k2/1250 + 176*k3/1875));
	k5 = MyF(xn+h*2/3, yn+h*(26*k1/81 + 7*k2/15 + 304*k3/4455 + 176*k4/297));
	k6 = MyF(xn+h, yn+h*(151*k1/150 + 351*k2/250 + 304*k3/4125 + 5*k4/77 + 243*k5/175));

	return yn+h*(k1/24 + 125*k4/336 + 27*k5/56 + 5*k6/48);
}

//Definimos la ecuación diferencial a trabajar 
float ODE(float x, float y)
{
	return x - y;
}

//Definimos la solución exacta
float exact(float x)
{
	return x - 1+2*exp(-x);
}


int main()
{
	int numPoints[4]={10, 100, 1000, 10000};

	//Definiendo condiciones iniciales
	float x0 = 0.0; float xf = 5.0; float y0 = 1.0;

	for (int i=0; i<4; i++)
	{
		//Definiendo h
		float h = (xf-x0)/numPoints[i];

		//Trabajando con vectores para la solución
		vector <float> y_sol, x_sol, Yy, diff;
		y_sol.push_back(y0);
		x_sol.push_back(x0);

		float xp=x0;
		while(xp<=xf)  //recorre los valores de x hasta llegar a xf 
		{
			float y = RK6(x_sol.back(), y_sol.back(), h, ODE);
			float y_ex = exact(x_sol.back());
			cout << xp << "," << y << "," << y_ex << "," << abs(y_ex-y) << endl;
			xp = x_sol.back() + h;
			y_sol.push_back(y); x_sol.push_back(xp);
			Yy.push_back(y_ex); diff.push_back(abs(y_ex-y));
		}

	}

	return 0;
}