#include <iostream>
#include <fstream>
using namespace std;

float MyF(float y, float x)
{  float MyF = x-y;
  return MyF;
    }

int main()
{

  int NumPuntos=10000;
  float x0=0.0;
  float xf=5.0;
  float y0=1.0;
  float h=(xf-x0)/NumPuntos;

  //Constantes de Runge Kutta
  
  float a21=1./3;
  float a31 = 123./256, a32 = 315./256;
  float a41=191/750, a42=184/1250, a43=176./1875;
  float  a51=26./81, a52=7./13, a53=304./4435, a54=175./291;
  float  a61=151./150, a62=351./250, a63=304./4123, a64=7./71, a65=245/173;

    
  float b1 = 1/24, b3 = 0;
  float b2 = 0, b4=125/336;
  float b5=27/56, b6=5./48;

  float  c2 = 1/3, c3 = 3/4, c4=1/5, c5=2/3, c6=1;


  //Se abre un archivo que guarda los resultados del Runge Kutta para cada uno de los pasos.
  
  ofstream Archivo;
  Archivo.open("RK6.txt");
  for(int i=0; i<=10000; i++)
    
    {

      //Definición del n-ésimo término de Runge Kutta.
      
  float k1 = MyF(y0, x0+i*h);
  float k2 = MyF(y0 + h*(a21*k1), x0+i*h + h*c2);
  float k3 = MyF(y0 + h*(a31*k1 + a32*k2), x0+i*h + h*c3);
  float k4 = MyF(y0 + h*(a41*k1 + a42*k2+a43*k3), x0+i*h + h*c4);
  float k5 = MyF(y0 + h*(a51*k1 + a52*k2+a53*k3+a54*k4), x0+i*h + h*c5);
  float k6 = MyF(y0 + h*(a61*k1 + a62*k2+a63*k3+a64*k4+a65*k5), x0+i*h + h*c6); ;
  //Se guardan los datos en el archivo de texto.
  
 Archivo << x0+i*h << " " << y0 << endl;
 
        y0= y0 + h*(b1*k1 + b2*k2 + b3*k3 + b4*k4 + b5*k5 + b6*k6);	
    }
  Archivo.close();
  return 0;
}
