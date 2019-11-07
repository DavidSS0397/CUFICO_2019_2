#include <iostream>
using namespace std;


float AX =0.0;
float AY=0.0;
float AZ=0.0;

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

void Particle::SetValues(float x,float y,float z,float vx,float vy, float vz,float m,int carga)
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
   X=X+(VX*t)+(0.5*ax*t*t);
   Y=Y+(VY*t)+(0.5*ay*t*t);
   Z=Y+(VZ*t)+(0.5*az*t*t);

   VX=VX +(t*0.5*(ax+AX));
   VY=VY +(t*0.5*(ay+AZ));
   VZ=VZ +(t*0.5*(az+AZ));

     

     }


float ax,ay,az;
int main()
{

  Particle A ;

  float BX=2,BY=3,BZ=4;

        cout<<" X "<<" Y "<< " Z "<<endl;
  A.SetValues(0,0,0,1.4,1.8,2.2,5.3,2);
   for (int i; i<20; i++)
    {
      ax=A.Carga*(A.VY*BZ-A.VZ*BY);
      ay=A.Carga*(A.VZ*BX-A.VX*BZ);
      az=A.Carga*(A.VX*BY-A.VY*BX);
      
      cout<<" "<<A.X<< " "<<A.Y<< " "<<A.Z<<" "<<endl;
      
      A.Pos_evol(ax,ay,az,1);

      AX=ax;
      AY=ay;
      AZ=az;

    }
 
 
 return 0;
}

