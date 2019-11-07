/*
Este codigo imprime la trayectoria de una particula con cierta velocidad en un campo magnetico, a partir del uso de clases de C++
*/

#include <iostream>
using namespace std;

//Se define la clase
class Particle
{

public:
  //Atributos
  int Carga;           //Carga 
  float X,Y,Z;         //Posicion
  float VX, VY, VZ;    //Velocidad
  float ax, ay, az;    //Aceleracion 
  float M;             //Masa

  //Metodos
  void Set_Values(float,float,float,float,float,float,float,int);
  float Pos_evol(float);
  float Vel_evol(float);
  float Mag_force(float, float, float);
  float Sistem_evol(int, float, float, float, float);
};

//Se fijan los valores de los atributos
void Particle::Set_Values(float x,float y,float z,float vx,float vy,float vz,float m,int Car)
{
  X=x;
  Y=y;
  Z=z;
  VX=vx;
  VY=vy;
  VZ=vz;
  M=m;
  Carga=Car;
}

//Calcula la evolucion de la posicion transcurrido un dt
float Particle::Pos_evol(float t)
{
  X = X+(VX*t)+(0.5*ax*(t*t));
  Y = Y+(VY*t)+(0.5*ay*(t*t));
  Z = Z+(VZ*t)+(0.5*az*(t*t));
}

//Calcula la evolucion de la velocidad transcurrido un dt
float Particle::Vel_evol(float t)
{
  VX = ax*t+VX;
  VY = ay*t+VY;
  VZ = az*t+VZ;
}

//Calcula la fuerza magnetica para luego fijar el atributo aceleraciones
float Particle::Mag_force(float Bx, float By, float Bz)
{
  int Fx = Carga*(VY*Bz-VZ*By);
  int Fy = -Carga*(VX*Bz-VZ*Bx);
  int Fz = Carga*(VX*By-VY*Bx);
  ax = Fx/M;
  ay = Fy/M;
  az = Fz/M;  
}

//Calcula e imprime la pos, vel y acel para ciertas iteraciones en cierto dt temporal. Evolucion del sistema.
float Particle::Sistem_evol(int iter, float dt, float Bx, float By, float Bz)
{
  //Loop de iteracciones
  for(int i=0; i<iter; i++)
    {
      Mag_force(Bx, By, Bz);     //Calculo aceleraciones
      Vel_evol(dt);              //Calculo velocidades 
      Pos_evol(dt);              //Calculo posiciones

      //Imprime en pantalla pos, vel, acel
      cout << X << " " << Y << " " << Z << " " << VX << " " << VY << " " << VZ << " " << ax << " " << ay << " " << az << endl;
    }
} 

int main()
{
  //Constante
  float m=10.0;                     //Masa
  int q=-1;                         //Carga
  //Condiciones iniciales
  float xo=0.0, yo=0.0, zo=0.0;    //Posicion       
  float vxo=10.0, vyo=0.0, vzo=10.0; //Velocidad
  //Campo magnetico
  float Bx=0.0, By=0.0, Bz=10.0;
  
  float dt=0.001;                  //Intervalo temporal
  float n=10000;                   //Iteraciones 

  //Se define la instancia de la clase
  Particle Particula1;  
  //Se fijan la condiciones iniciales
  Particula1.Set_Values(xo, yo, zo, vxo, vyo, vzo, m, q);
  //Se calcula la evolucion del sitema
  Particula1.Sistem_evol(n, dt, Bx, By, Bz);
  
  return 0;
}
