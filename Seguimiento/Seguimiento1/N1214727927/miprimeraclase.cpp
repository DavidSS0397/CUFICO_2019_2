#include <iostream>
using namespace std;

class Particula
{
public:
  int Carga;
  float X;
  float Y;
  float Z;
  float Vx,Vy,Vz;
  float Ax,Ay,Az;
  float M;
  void setvalues(float,float,float,float,float,float,float,int);
  float descripcion(float,float,float);
};


void Particula::setvalues(float x, float y, float z, float vx, float vy, float vz, float m, int carga)
{
  X=x;
  Y=y;
  Z=z;
  Vx=vx;
  Vy=vy;
  Vz=vz;
  Carga=carga;
  M=m;

}

float Particula::descripcion(float bx, float by, float bz)
{
  int t0=0;
  for (int  t=0; t<=100; t++)
    {
      cout << "t:" << t << endl;
      Ax=(Carga*(Vy*bz-Vz*by))/M; //aceleracion de la particula
      Ay=(Carga*(Vz*bx-Vx*bz))/M;
      Az=(Carga*(Vx*by-Vy*bx))/M;

      Vx=Vx+Ax*(t-t0); //velocidad de la particula
      Vy=Vy+Ay*(t-t0);
      Vz=Vz+Az*(t-t0);

      X=X+Vx*(t-t0)+0.5*Ax*(t-t0)*(t-t0); //posicion de la particula
      Y=Y+Vy*(t-t0)+0.5*Ay*(t-t0)*(t-t0);
      Z=Z+Vz*(t-t0)+0.5*Az*(t-t0)*(t-t0);
      t0=t;
    
      cout << "x:" << X << " " << "y:" << Y << " " << "z:" << Z << endl;
      cout << "Vx:" << Vx << " " << "Vy:" << Vy << " " << "Vz:" << Vz << endl;
      cout << "Ax:" << Ax << " " << "Ay:" << Ay << " " << "Az:" << Az << endl;
    }
}
  
int main()
{
  Particula Particula1;

   cout << "m:" << Particula1.M << " " << "carga:" << Particula1.Carga << " " \
	<< "x:" << Particula1.X << " " << "y:" << Particula1.Y << " "	\
	<< "z:" << Particula1.Z << " " << "vx:" << Particula1.Vx << " "	\
	<< "vy:" << Particula1.Vy << " " << "vz:" << Particula1.Vz << endl ; //antes de dar los valores
  
  Particula1.setvalues(0.0,0.0,0.0,10.0,0.0,0.0,1000.0,10);
  
   cout << "m:" << Particula1.M << " " << "carga:" << Particula1.Carga << " "\
	<< "x:" << Particula1.X << " " << "y:" << Particula1.Y << " "	\
	<< "z:" << Particula1.Z << " " << "vx:" << Particula1.Vx << " "	\
	<< "vy:" << Particula1.Vy << " " << "vz:" << Particula1.Vz << endl ;
  
   Particula1.descripcion(0.0,0.0,10.0); //campo en bz=10

  return 0;
}
