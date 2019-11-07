/* RK6.cpp y RK6.py
   Solucionar Rk6 en c++ que saque un archivo de texto con los digitos de la solucion y un codigo en python que tome este archivo de texto y los grafique en matplot las mismas tres graficas de esta clase (Solo comparación de la Rk6 con la exacta de y' = x - y */

#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

double ExactSol(double x)     //Solución exacta
{ double y = x - 1+2*exp(-x); 
  return y;}

double F(double x,double y){return (x-y);}//La ODE

template <typename T>        //Esto es un np.linspace hecho a mano con ayuda de internet
std::vector<T> linspace(T a, T b, size_t N) {
    T h = (b - a) / static_cast<T>(N-1);
    std::vector<T> xs(N);
    typename std::vector<T>::iterator x;
    T val;
    for (x = xs.begin(), val = a; x != xs.end(); ++x, val += h)
        *x = val;
    return xs;}

double rk6(double xn, double yn, double h){ //Método de Runge kutta 6
  std::vector <double> c,b,k,a2,a3,a4,a5,a6; //vectores tipo double
 a2 = {0,1./3.};                                  //a21,a22...
 a3 = {0,123./256.,315./256.};                    //a31,a32... 
 a4 = {0,193./750,189./1250.,176./1875.};         //
 a5 = {0,26./81.,7./15.,304./4455.,175./297.};
 a6 = {0,151./150.,351./250.,304./4125.,5./77.,243./175.};
 b = {0,1./24.,0.,0.,125./336.,27./56.,5./48.};
 c = {0,1./3.,3./4.,1./5.,2./3.,1.};
 
 double xn1,yn1,k1,k2,k3,k4,k5,k6; //Declaramos variables tipo double
 
    xn1 = xn + h;
    k1= F(xn,yn);
    k2 = F(xn + h*c[2],yn + h*a2[1]*k1);
    k3 = F(xn + h*c[3],yn + h*(a3[1]*k1+a3[2]*k2));
    k4 = F(xn + h*c[4],yn + h*(a4[1]*k1 + a4[2]*k2 + a4[3]*k3));
    k5 = F(xn + h*c[5],yn + h*(a5[1]*k1 + a5[2]*k2 + a5[3]*k3 + a5[4]*k4));
    k6 = F(xn + h*c[6],yn + h*(a6[1]*k1 + a6[2]*k2 + a6[3]*k3 + a6[4]*k4 + a6[5]*k5) );
    
    yn1 = yn + h*(b[1]*k1 + b[2]*k2 + b[3]*k3 +b[4]*k4 + b[5]*k5 + b[6]*k6);
		  
    return yn1;}

int main()
{  
  std::vector <double> h(1),numpuntos; //Vectores para los puntos de división de la gráfica
  double xf,xi,yi;
  numpuntos = {10,100,1000,10000};
  xf = 5.;
  xi = 0.;
  yi = 1.;
  for (int i=0; i<numpuntos.size(); i++)
    {h[i] = ((xf - xi)/numpuntos[i]);}
  std::cout<<"X,Y,Yexacta,Diff"<<std::endl;

  //Empezamos a buscar soluciones:
  double k = 0;
  for (k; k<numpuntos.size();k++){ //Desde aquí empieza lo sabroso
       double j = numpuntos.back();
       
       std::vector <double> rk6Solutions,ExactSolutions,DiffSolutions,xs;//Declaramos los vectores
	  
       xs = linspace(xi,xf,j);//Usamos la funcion linspace para generar x
	  rk6Solutions.push_back(yi);
	  for (int n = 0; n<xs.size();n++){

	    double rkCS = rk6(xs[n], rk6Solutions.back(), ((xf - xi)/j));
	    rk6Solutions.push_back(rkCS);
	      
	    double ExactCS = ExactSol(xs[n]);
	    ExactSolutions.push_back(ExactCS);
	    
	    DiffSolutions.push_back(rkCS - ExactCS);
	  
	    std::cout<< xs[n] <<","<< rkCS << "," << ExactCS << "," << (rkCS - ExactCS) <<std::endl;  
	  }
	}
    
  return 0;}

