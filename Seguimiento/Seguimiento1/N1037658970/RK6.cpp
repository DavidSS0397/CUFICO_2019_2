/*
! ===========================================================================
! RK6.cpp
! ===========================================================================
! Este programa soluciona la ecuacion diferencial y'=x-y usando RK6
!     Valentina Roquemen Echeverry, valentina.roquemen@udea.edu.co

! Up to date: 19 septiembre 2019			
*/

#include <iostream>
using namespace std;

/*
Funcion que calcula y_n+1 con RK6
Input: x_n,y_n, h->Paso, ODE->Funcion con ecuacion diferencial
Return: y_n+1
*/
float RK6(float x, float y, float h, float (*ODE)(float,float))
{
	float k1,k2,k3,k4,k5,k6;
	float c2,c3,c4,c5,c6,a21,a31,a32,a43,a42,a41,a54,a53,a52,a51,a65,a64,a63,a62,a61,b1,b2,b3,b4,b5,b6;
	c2 = 1./3; c3 = 3./4; c4 = 1./5; c5 = 2./3; c6 = 1.;
	b1 = 1./24; b2 = 0; b3 = 0; b4 = 125./336; b5 = 27./56; b6 = 5./48;
	a21 = 1./3; a31 = 123./256; a32 = 315./256; a41 = 193./750; a42 = 189./1250; a43 = 176./1875; a51 = 26./81; a52 = 7./15; a53 = 304./4455; a54 = 176./297; a61 = 151./150; a62 = 351./250; a63 = 304./4125; a64 = 5./77; a65 = 243./175;

	k1 = ODE(x, y);
	k2 = ODE(x+h*c2, y+h*a21*k1);
	k3 = ODE(x+h*c3, y+h*(a31*k1+a32*k2));
	k4 = ODE(x+h*c4, y+h*(a41*k1+a42*k2+a43*k3));
	k5 = ODE(x+h*c5, y+h*(a51*k1+a52*k2+a53*k3+a54*k4));
	k6 = ODE(x+h*c6, y+h*(a61*k1+a62*k2+a63*k3+a64*k4+a65*k5));

	return y+h*(b1*k1+b2*k2+b3*k3+b4*k4+b5*k5+b6*k6);
}

/*
Funcion con ecuacion diferencial
Input: x,y
Return: x-y
*/
float ODE(float x, float y)
{
	return x-y;
}

int main()
{
	//Definicion de variables
	float x0,xf,y0,h;
	int NumPuntos[4] = {10,100,1000,10000};
	float x, y_RK6;

	//Condiciones iniciales
	x0 = 0.; xf = 5.; y0 = 1.;  

	//Calculo de la solucion para diferente numero de puntos
	for (int j = 0; j<4; j++)
	{

		x = x0; y_RK6 = y0;
		cout << x <<","<< y_RK6<< endl;
		h = (xf-x0)/NumPuntos[j];
		for (float i = 1; i < NumPuntos[j]; i++)
		{
			y_RK6 = RK6(x,y_RK6,h, ODE);
			x += h;
			cout << x <<","<< y_RK6<< endl;
			
		}
	}	
  return 0;
}
