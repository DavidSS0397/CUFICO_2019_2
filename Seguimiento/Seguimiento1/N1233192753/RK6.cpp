#include <iostream>
using namespace std ;

float F(float y,float x)
{
    return x-y;                     //Ecuacion diferencial 
}

float RK6 (float xn, float yn, float h)        // Runge-Kuta de orden 6
{ 
    float k1 = F(yn, xn );
    float k2 = F(yn + h*(k1*1./3), xn + h*(1./3));
    float k3 = F(yn + h*(k1*123./256 + k2*315./256), xn + h*(3./4));        
    float k4 = F(yn + h*(k1*191./750 + k2*184./1250 + k3*176./187), xn + h*(1./5));     
    float k5 = F(yn + h*(k1*26./81 + k2*7./15 + k3*304./4455 + k4*175./297), xn + h*(2./3));
    float k6 = F(yn + h*(k1*151./150 + k2*351./250 + k3*304./4125 + k4*7./77 + k5*243./175), xn + h); 
    
    float yn1 = yn + h*( k1*1./24 + k2*0 + k3*0 + k4*125./336 + k5*27./56 + k6*5./48);

    return yn1;
}

int main()
{  
    float x0 = 0.0;
    float xf = 5.0;       // Condiciones iniciales 
    float y0 = 1.0;

    int NumPuntos[4] = {10.,100.,1000.,10000.};  


     for( int j=0; j<=3 ; j++)
     {
         float h = (xf - x0)/NumPuntos[j];  // Paso

         for ( int i=0; i <= NumPuntos[j]; i++)
        {
            float yn = RK6(x0,y0,h);             // Calculo valor yn 
            float xn = x0 + h;                  // Calculo valor xn
            cout << xn << " " << yn <<endl;     
            x0 = xn;                                //Redefinicion de vlores iniciales             
            y0 = yn;             
        }  
        x0 = 0.0;
        xf = 5.0;
        y0 = 1.0; 
     }
    return 0;
}
