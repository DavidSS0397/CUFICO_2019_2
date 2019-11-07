#include <iostream>
using namespace std;

class Particle
{
  
public:
  int Carga;
  float X,Y,Z;
  float VX,VY,VZ;
  float M;
  void SetValues(float,float,float,float,float,float,float,int);
  float Pos_evol(float,float,float,float);
};

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

float Particle::Pos_evol(float Bx, float By, float Bz, float t)
{
  float ax,ay,az;

  //Cinematic equations obtained via Taylor Series expansion of order 1
  
  ax = Carga/M * (VY*Bz - VZ*By);
  ay = Carga/M * (VZ*Bx - VX*Bz);
  az = Carga/M * (VX*By - VY*Bx);
 
  VX += ax*t;
  VY += ay*t;
  VZ += az*t;
  
  X += (VX*t);
  Y += (VY*t);
  Z += (VZ*t);
}
  
int main()
{
  Particle Particula;

  Particula.SetValues(0.0,0.0,0.0,1.0,1.0,0.0,2.0,1);

  int iter = 1000;
  cout << "X" << "," << "Y" << "," << "Z" << endl; //I did this to create a .csv so I could plot the results with python
  for (int i = 0; i < iter; i++)
    {
      Particula.Pos_evol(0.0,0.0,10.0,0.01);
      cout << Particula.X << "," << Particula.Y << "," << Particula.Z << endl; 
    }

  return 0;
}
