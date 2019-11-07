/*
Script que computa la evolucion espacial de una particula cargada bajo la influencia de un campo magnetico constante en direccion z con velocidad inicial diferente de cero
*/

#include <iostream>
using namespace std;

class Particle
{
public:
  
  int Q, B;
  float X, Y, Z, VX, VY, VZ, M;

  void InitialCond(float, float, float, float, float, float, float, int, int);
  void Evol(int);

};

void Particle::InitialCond(float x, float y, float z, float vx, float vy, float vz, float m, int q, int b)
{
  X=x; Y=y; Z=z; VX=vx; VY=vy; VZ=vz; M=m; Q=q;
}


void Particle::Evol(int time) // solo imprime 
{
  // evolucion por diferenciales
  // imprimir la evoolucion (print dentro del for)

  float ax, ay, az;
  
  
 for(float t=0; t<time; t+=1)
{
  ax=Q*VY*B/M;
  ay=-Q*VX*B/M;
  az=0;

  VX+=ax*t; VY+=ay*t;
  X+=VX*t; Y+=VY*t;
  Z+=VZ*t;

  cout  << "Posiciones, tiempo : " << t << endl;
  cout  << X << " " << Y << " " << Z << endl;
  
   }
 
}

int main()
{

  Particle P;
  
  P.InitialCond(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2, 1);
  P.Evol(3);

}
