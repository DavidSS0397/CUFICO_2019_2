#include<iostream>
#include<fstream>
using namespace std;

float F(float y, float x)
{  
    float MyF = x-y;
    return MyF;
}



int main()

{ 
    int Numpuntos=10000;

    float x0=0.; //limites de la funcion (inferior)
    float xf=5.; //limites de la funcion (superior)
    float y0=1.0;
    float h=(xf-x0)/Numpuntos;


    //coeficientes 
    float a21=1./3;
    float a31 = 123./256, a32 = 315./256;
    float a41=193./750, a42=189./1250, a43=176./1875;
    float  a51=26./81, a52=7./15, a53=304./4455, a54=175./297;
    float  a61=151./150, a62=351./250, a63=304./4125, a64=7./77, a65=243./175;

    
    float b1 = 1./24, b3 = 0.;
    float b2 = 0., b4=125./336;
    float b5=27./56, b6=5./48;

    float  c2 = 1./3, c3 = 3./4, c4=1./5, c5=2./3, c6=1.;

    // evaluacion del metodo de RK6
    int i;
	ofstream File;
  	File.open ("RKtt6.txt");//escritura de datos
  		
  	for(i=0; i<=10000; i=i+1)
	{
        
        float k1 = F(y0, x0+ i*h);
        float k2 = F(y0 + h*(a21*k1), x0+ i*h + h*c2);
        float k3 = F(y0 + h*(a31*k1 + a32*k2), x0+ i*h + h*c3);
        float k4 = F(y0 + h*(a41*k1 + a42*k2+a43*k3), x0+ i*h + h*c4);
        float k5 = F(y0 + h*(a51*k1 + a52*k2+a53*k3*a54*k4), x0+ i*h + h*c5);
        float k6 = F(y0 + h*(a61*k1 + a62*k2+a63*k3*a64*k4+a65*k5), x0+ i*h + h*c6);
   
                
     
	//se imprime en el archivo los pares x,y.
        File << x0+i*h << " " << y0 << endl;
	//se redefine el valor para y0
        y0=y0 + h*(b1*k1 + b2*k2 + b3*k3 + b4*k4 + b5*k5 + b6*k6);	   	
        }
		File.close();
		return 0;
}
