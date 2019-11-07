#include <iostream>
#include<fstream>
using namespace std;

float MyF(float y, float x)
{
  float f=x-y;
  return f;
}
  

int main()
{

    //Condiciones Iniciales
    float x0=0.;
 float xf=5.;
 float y0=1.0;

 //Paso
 float h=(xf-x0)/10000;
 
 
  
 float a21=1./3, a31=123./256 , a32=315./256 , a41=193./750, a42=189./1250, a43=176./1875, a51=26./81, a52=7./15, a53=304./4455, a54=17./297, a61=151./150, a62=351./250, a63=304./4125, a64=5./77, a65=243./175 ;
  
  float b1=1./24, b3=0 , b2=0. , b4=125./336 , b5=27./56 , b6=5./48;
  
  float c2=1./3, c3=3./4, c4=1./5, c5=2./3, c6=1.;

  //Calculo de Runge Kutta 6, en vez de agregar los calculos a una lista se copiaran directamente en un archivo de texto
  int i;
  ofstream myfile;
  myfile.open ("RK6.txt");

  for (i=0; i<=10000; i=i+1){
    float k1= MyF(y0, x0+i*h);
    float k2= MyF(y0 + h*(a21*k1),x0+(i*h)+(h*c2));
    float k3= MyF(y0 + h*(a31*k1 + a32*k2),x0+(i*h)+(h*c3));
    float k4= MyF(y0 + h*(a41*k1 + a42*k2 + a43*k3),x0+(i*h)+(h*c4));
    float k5= MyF(y0 + h*(a51*k1 + a52*k2 + a53*k3 + a54*k4),x0+(i*h)+(h*c5));
    float k6= MyF(y0 + h*(a61*k1 + a62*k2 + a63*k3 + a64*k4 + a65*k5),x0+(i*h)+(h*c6));

    myfile << x0+i*h << " " << y0 <<endl;
    y0=y0+h*(b1*k1 + b2*k2 + b3*k3 + b4*k4 + b5*k5 + b6*k6);

  }
  myfile.close();

  
    
  return 0 ;
  }
