#include<iostream>
using namespace std;

/*
struct PosicionYCarga //analogo a la lista de python
{
  int Carga;
  float X;
  float Y;
  float Z;
}
  Particula1, Particula2; //instancias 
// punto para acceder a atributos o metodos
// -> para los punteros
*/

class Particle
{
public: //desde cualquier parte del codigo se puede acceder tambien hay privado y restringido 
  int Carga;
  float X,Y,Z;
  float VX,VY,VZ;
  float M;
  void SetValues(float,float,float,float,float,float,float,int);
  //metodo es algo activo en la clase ya que es una funcion en una clase
  float Pos_evol(float,float,float,float); //que tipo de argumentos espera y cuantos espera sin saber cuales son si uno es X o VX

}; //(se debe poner ; alfinal de la clase)
// se pueden declarar instancias aca  eje: P1,P2;

void Particle::SetValues(float x, float y, float z, float vx, float vy, float vz, float m, int carga) //la funcion setvalues esta declarada en particle
{
  X=x;
  Y=y;
  Z=z;
  VX=vx;
  VY=vy;
  VZ=vz;
  M=m;
  Carga=carga;
  //esta funcion es para asignar valores
}
void SumaAlPrimero(int a, int b)
{ a = a+b;
}

//esc + x query replace  para cambiar 1 por un 3 por ejemplo practicamente en todas las partes del codigo

float Particle::Pos_evol(float ax,float ay, float az, float t)
{
  X=X+(VX*t)+(0.5*ax*t*t);
  Y=Y+(VY*t)+(0.5*ay*t*t);
  Z=Z+(VZ*t)+(0.5*az*t*t);
  
  VX=VX+ax*t;
  VY=VY+ay*t;
  VZ=VZ+az*t;
  //return t;
}

struct MagneticField
{
 float Bx;
 float By;
 float Bz;
}
  MagneticFieldz;

int main()
{
  //deifnimos los valores para struct definido anteriormente
  MagneticFieldz.Bx=0;
  MagneticFieldz.By=0;
  MagneticFieldz.Bz=10;
		      
     
  // float y= SumaSimple(t,k);
  //cout << y << endl;
  //cout << t << endl;
  
  //cout << t << endl;  return 0;
  
  
  Particle Particula; //para crear una instancia


  
  cout << Particula.Carga << " " << Particula.X << " " << Particula.Y << " "  << Particula.Z << endl;
  
  Particula.SetValues(0.0,0.0,0.0,1.0,0.0,1.0,5.0,1);

  cout << Particula.Carga << " " << Particula.X << " " << Particula.Y << " "  << Particula.Z << endl;

  float AX=0, AY=0, AZ=0;
  
  for (int i=0; i<70; i++)

    {
      float t=0, dt=0.001; 
      //para el producto cruz en la fuerza de lorentz
      SumaAlPrimero(t,dt);
      
      AX = Particula.Carga*(Particula.VY*MagneticFieldz.Bz-Particula.VZ*MagneticFieldz.By)/Particula.M;

      AY = Particula.Carga*(Particula.VZ*MagneticFieldz.Bx-Particula.VX*MagneticFieldz.Bz)/Particula.M;

      AZ = Particula.Carga*(Particula.VX*MagneticFieldz.By-Particula.VY*MagneticFieldz.Bx)/Particula.M;

      //cout << AX << " " << AY << AZ << endl;
	
      Particula.Pos_evol(AX,AY,AZ,0.1); //arg final dt=0.1
      //Las posiciones se actualizan con la funcion pos_evol pero las velocidades deben actualizarse tambien

      cout << t << endl;

      cout << Particula.X << " " << Particula.Y << " "  << Particula.Z << endl;
      //cout << Particula.VX << " " << Particula.VY << " "  << Particula.VZ << endl;
      
    }  
  return 0;
}

