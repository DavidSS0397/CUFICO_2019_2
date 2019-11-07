#include <iostream>
using namespace std;

class Particle
{
public:
  int Carga;
  float X,Y,Z;
  float VX,VY, VZ; //el campo esta en la direccion Z, luego no hay az
  float AX,AY;
  float M;
  float B;
  void SetValues(float, float, float, float, float, float, float, float, int);
  float Pos_evol(float);

};

void  Particle::SetValues(float x, float y, float z, float vx, float vy, float vz, float m, float b, int carga)
{
  X=x;
  Y=y;
  Z=z;
  VX=vx;
  VY=vy;
  VZ=vz;
  M=m;
  B=b;
  Carga=carga;
}

float Particle::Pos_evol(float t)
{
  AX=(VY*B)/M; //como la carga es 1 no necesito ponerla
  AY=(-VX*B)/M;
  VX=VX+(AX*t);
  VY=VY+(AY*t);
  X=X+(VX*t)+(0.5*AX*t*t);
  Y=Y+(VY*t)+(0.5*AY*t*t);
  Z=Z+(VZ*t);
}


int main()
{
  Particle Particula;
  Particula.SetValues(0.0,0.0,0.0,1.0,1.0,1.0,5.0,10.0,1.0);
  
  for (int i=0; i<=10000; i+=1)
    {
      Particula.Pos_evol(0.01);
      cout << Particula.X << " " << Particula.Y << " " << Particula.Z << endl;
    }
            
  return 0;
}
