#include <iostream>
#include <vector>
#include <stdio.h>
FILE *output;       // Esto es lo que va a permitir exportar los datos a un archivo de texto.
using namespace std;

//Método RK6

//Ecuación diferencial y' = x-y  

float ODE(float x, float y)
{
  return (x-y);
}

float RK6(float x0, float y0, float xn, float n)  // Se define el rk6 
{
  float k1,k2,k3,k4,k5,k6;
  float b1 = 1/24;
  float b2 = 0;
  float b3 = 0;
  float b4 = 125/336;
  float b5 = 27/56;
  float b6 = 5/48;
  float h = (xn - x0)/n;
  float yn = y0;
  for (int i=1; i<=n; i++)
    {
      xn = xn + h;

      k1 = ODE(xn,yn);
      k2 = ODE(xn + h/3, yn + h*(k1/3));
      k3 = ODE(xn + h*(3/4), yn + h*((123/256)*k1 + (315*k2)/256));
      k4 = ODE(xn + h/5, yn + h*((193/750)*k1 + (198/1250)*k2 + (176/1875)*k3));
      k5 = ODE(xn + h*(2/3), yn + h*((26/81)*k1 + (7/15)*k2 + (304/4455)*k3 + (175/297)*k4));
      k6 = ODE(xn + h, yn + h*((151/150)*k1 + (351/250)*k2 + (304/4125)*k3 + (5/77)*k4 + (243/175)*k5));
      yn = yn + h*(b1*k1 + b2*k2 + b3*k3 + b4*k4 + b5*k5 + b6*k6);
    }
    return yn;
}

int main()
{
  output = fopen("datos.txt", "a+");   // Le decimos al programa que abra un archivo en el que se puede leer y escribir.
  float h = 0.005;   //Ancho del intervalo
  float n = 10000;  //Número de puntos
  float x0 = 0;    // Condiciones iniciales
  float y0 = 1;
  float xs = x0;
  for (int i=0; i<=n; i++)
    {                                                                                                                           
      xs += h;     
      fprintf(output, "%0.2f    %0.2f\n", xs, RK6(x0,y0,xs,n));  // Exporta los datos a un archivo de texto llamado datos.txt
                                                                 // el cual tiene 2 columnas, los valores de x y los valores de
                                                                 // yn a partir del rk6
    }
}
