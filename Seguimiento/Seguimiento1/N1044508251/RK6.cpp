#include <iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;

//Derivada a solucionar
float MyF(float y, float x)
{
  return x-y;
}

//Metodo de RK6
float RK6(float xn, float yn, float h, float (*MyF)(float, float))
{
  
  float c2 = 1./3, c3 = 3./4, c4 = 1./5, c5 = 2./3, c6 = 1.;
  float a21 = 1./3, a31 = 123./256, a41 = 193./750, a51 = 26./81, a61 = 151./150;
  float a32 = 315./256, a42 = 189./1250, a52 = 7./15, a62 = 351./250;
  float a43 = 176./1875, a53 = 304./4455, a63 = 304./4125;
  float a54 = 175./297, a64 = 5./77;
  float a65 = 243./175;
  float b1 = 1./24, b2 = 0, b3 = 0, b4 = 125./336, b5 = 27./56, b6 = 5./48;

  float k1, k2, k3, k4, k5, k6; 

  k1 = MyF(yn, xn);
  k2 = MyF(yn + h*a21*k1, xn + h*c2);
  k3 = MyF(yn + h*(a31*k1 + a32*k2), xn + h*c3);
  k4 = MyF(yn + h*(a41*k1 + a42*k2 + a43*k3), xn + h*c4);
  k5 = MyF(yn + h*(a51*k1 + a52*k2 + a53*k3 + a54*k4), xn + h*c5);
  k6 = MyF(yn + h*(a61*k1 + a62*k2 + a63*k3 + a64*k4 + a65*k5), xn + h*c6);
  
  float yn1 = yn + h*(b1*k1 + b2*k2 + b3*k3 + b4*k4 + b5*k5 + b6*k6);

  return yn1;
}
  
int main()
{     
  int NumPuntos[4] = {10, 100, 1000, 10000}; //Arreglo para la cantidad de puntos
  float x0 = 0.0, xf = 5.0, y0 = 1.0;        //Condiciones iniciales

  for(int k=0; k<=3; k+=1){                  //Loop para barrer los diferentes cantidad de puntos

    float h = (xf - x0)/NumPuntos[k];        //Paso 
    
    for(int i=0; i<=NumPuntos[k]; i+=1)      //Calculo de Y por RK6 para cada cantidad de puntos
       {
	cout << x0 << " " << y0 << endl;     // Salida de valores
      
	float xn1, yn1;

	xn1 = x0 + h;
	yn1 = RK6(x0, y0, h, MyF);
	
      
	x0 = xn1;
	y0 = yn1;
      }

    x0=0.0;                                  //Reinicio de condiciones de iniciales
    xf=5.0;
    y0=1.0;
  }
    
  return 0;
}
