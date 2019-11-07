/*  SEGUIMIENTO 3:
 
    Script con clases y toda la vaina para una particula cargada interactuando en un campo magnético constante con velocidad inicial diferente de cero.*/

#include <iostream>
using namespace std; //Por simplicidad

class Particula //Defino una clase para particula
{
public:
  int Carga;
  float M, X, Y, Z, VX, VY, VZ;
  void SetValues(int,float,float, float, float,float,float,float);
};

class CampoM //Otra clase es el campo
{
public:
  float Bx, By, Bz;
  void SetValues(float, float, float);
};

void Interaccion(float x, float y, float z,float vx, float vy, float vz, float bx, float by, float bz, float m, int q)
{
  float Ax, Ay, Az;
  float Fx, Fy, Fz;
  Particula p1,p2;
  p1.Carga = q;
  p1.X=x;
  p1.Y=y;
  p1.Z=z;
  p1.VX=vx;
  p1.VY=vy;
  p1.VZ=vz;
  p1.M=m;

  CampoM b1;
  b1.Bx=bx;
  b1.By=by;
  b1.Bz=bz;
  
  for(float t=0; t<11; t+=1)
{  
  Fx = q*(vy*bz - vz*by);
  Fy = q*(vz*bx - vx*bz);
  Fz = q*(vx*by - vy*bx);

    //Método de Euler
  Ax=Fx/m;
  vx+=Ax*t;
  x+=vx*t;

  Ay=Fy/m;
  vy+=Ay*t;
  y+=vy*t;

  Az=Fz/m;
  vz+=Az*t;
  z+=vz*t;
  std::cout<< "En tiempo: " << t << " la posicion en x es: " << x << std::endl;
 
  
 } 
    }

int main()
{ 
  // Interaccion(p1.X,p1.Y,p1.Z,p1.VX,p1.VY,p1.VZ,b1.Bx,b1.By,b1.Bz,p1.M,p1.Carga);
Interaccion(1,0,0,1,0,0,0,0,1,1,1);//x,y,z,vx,vy,vz,Bx,By,Bz,M,Q

    return 0;
    } 

