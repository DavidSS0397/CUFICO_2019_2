/*
! ===========================================================================
! MiPrimeraClase.cpp
! ===========================================================================
! Este programa describe la evolucion de la posicion de una particula inmersa en
! un campo magnetico.
!     Valentina Roquemen Echeverry, valentina.roquemen@udea.edu.co

! Up to date: 5 septimbre 2019			
*/

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
    float PosEvol(float,float,float,float);
};

/**Valores iniciales de los atributos de la particula*/
void Particle::SetValues(float x,float y, float z, float vx, float vy, float vz, float m, int car)
{
  //Posicion inicial
  X = x;
  Y = y;
  Z = z;
  //Velocidad inicial
  VX = vx;
  VY = vy;
  VZ = vz;
  M = m; //Masa
  Carga = car; //Carga
}

/*Evolucion de la posicion de una particula*/
float Particle::PosEvol(float Fx, float Fy, float Fz,float t )
{
  float ax,ay,az; 
  ax = Fx/M ; ay = Fy/M ; az = Fz/M ; //Aceleraciones
  VX += ax*t; VY += ay*t; VZ += az*t; //Velocidades

  //Posiciones
  X = X+(VX*t) + (0.5*ax*(t*t));
  Y = Y+(VY*t) + (0.5*ay*(t*t));
  Z = Z+(VZ*t) + (0.5*az*(t*t));
}

/*Fuerza de una particula bajo un campo magnetico*/
void FuerzaMagentica(float Bx, float By, float Bz, float VX,float VY, float VZ, float q,float &Fx, float &Fy, float &Fz)
{
	Fx = q*(VY*Bz-VZ*By);
	Fy = q*(VZ*Bx-VX*Bz);
	Fz = q*(VX*By-VY*Bx);
}

int main()
{
	float Fx, Fy, Fz; //Variable para las fuerzas
	float Bx = 0, By = 0, Bz = 10; //Campo magnetico
	int T = 1000; //Numero de iteraciones
	float dt = 0.01; //Intervalo temporal
	Particle Particula; //Definicion de la particula

	//Valores iniciales para la particula
	//x,y,z,vx,vy,vz,m,carga
  	Particula.SetValues(0.0,0.0,0.0,1.0,1.0,0.0,2,1);


  	//Evolucion temporal
 	cout << "X     |  Y    |  Z" <<endl;
  	for (int i = 0; i<T ; i++ )
  	{ 		
	  	FuerzaMagentica(Bx,By,Bz,Particula.VX,Particula.VY,Particula.VZ,Particula.Carga, Fx,Fy,Fz);
  		Particula.PosEvol(Fx,Fy,Fz,dt);
	  	cout << Particula.X <<"|"<< Particula.Y<<" |"<< Particula.Z<< endl;
	}
  return 0;
}
