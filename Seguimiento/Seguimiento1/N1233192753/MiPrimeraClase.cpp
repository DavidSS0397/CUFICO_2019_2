#include <iostream>
using namespace std ;

class Particle
{
public:
  int Carga;
  float X, Y, Z;
  float VX, VY, VZ;              //clase 
  float M;

  
  void SetValues(float, float, float, float, float, float, float, int);
  float Pos_evol(float, float, float, float);
  float Vel_evol(float, float, float, float);

} P1;

void Particle::SetValues(float x, float y, float z, float vx, float vy, float vz, float m, int carga)
{
  X=x;
  Y=y;
  Z=z;
  VX=vx;
  VY=vy;
  VZ=vz;
  M=m;
  Carga=carga;
}

float Particle::Pos_evol(float ax, float ay, float az, float t)
{
  X=X+(VX*t)+(0.5)*ax*t*t;
  Y=Y+(VY*t)+(0.5)*ay*t*t;         // Evolucion temporal posicion 
  Z=Z+(VZ*t)+(0.5)*az*t*t;  
  return X;
  return Y;
  return Z;
}

float Particle::Vel_evol(float ax, float ay, float az, float t)
{
    VX=VX+(ax*t); 
    VY=VY+(ay*t);
    VZ=VZ+(az*t);           // Evolucion temporal velocidad 
    return VX;
    return VY;
    return VZ;
}

float Ace(float v0_1, float v0_2, float B_1, float B_2, float m, int carga)
{
    float a= carga*(v0_1*B_2-v0_2*B_1)/m;      // calculando componete i de la acelaracion 
    return a;

}

int main()
{     
    float dt=0.001;    // paso de tiempo
    int Bx=0, By=0, Bz=3;  // Campo Magnetico 

    P1.SetValues(1.0,1.0,1.0,1.0,0.0,1.0,4.0,1);  // Valores iniciales 

    float ax, ay, az;
    
    int i=0;
    while (i<=100000)
    {
        ax = Ace(P1.VY, P1.VZ, By, Bz, P1.M, P1.Carga);  
        ay = Ace(P1.VZ, P1.VX, Bz, Bx, P1.M, P1.Carga);    // calculo aceleraciones 
        az = Ace(P1.VX, P1.VY, Bx, By, P1.M, P1.Carga);
        
        P1.Vel_evol(ax, ay, az,dt);    // calculo posiciones 

        P1.Pos_evol(ax, ay, az, dt);   // calculo velociades 

        cout << P1.X << "  " << P1.Y << "  " << P1.Z << "  " << P1.VX << "  " << P1.VY << "  " << P1.VZ << "  " << ax << "  " << ay << "  " << az << endl;   // resultados en pantalla 

        i++;

    }

    return 0;
}

