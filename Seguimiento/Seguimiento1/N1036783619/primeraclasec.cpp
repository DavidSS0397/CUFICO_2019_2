#include <iostream>
using namespace std;
class particle //define la clase donde se determinan las propiedades de las partículas
{
public:
  int Carga;
  float X, Y, Z;
  float VX, VY, VZ;
  float M;  
  void setvalues( float, float, float, float, float, float, float, int);
  float pos_evol( float, float, float, float); //determina la evolución de la posición
  float vel_evol( float, float, float, float);//determina la evolución de la velocidad 
} B;
void particle::setvalues(float x, float y, float z, float vx, float vy, float vz, float m, int carga)//función que determina los valores de las propiedades de la partícula
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

float particle::pos_evol(float ax, float ay, float az, float t) //función cinemática de la posición
{
  X=X+(VX*t)+(0.5*ax*t*t);
  Y=Y+(VY*t)+(0.5*ay*t*t);
  Z=Z+(VZ*t)+(0.5*az*t*t);
  return t;
}
float particle::vel_evol(float ax, float ay, float az, float t)//función cinemática de la velocidad
{
  VX = VX + ax*t;
  VY = VY + ay*t;
  VZ = VZ + az*t;

  return t;
}

int main() //bloque de código para la simulación de la partícula en el campo magnético uniforme
{
  float t=0.0; //tiempo inicial y paso de tiempo para el bucle
  float dt=0.1;
  //se definen las componentes del campo magnético
  B.X=5.6;
  B.Y=4.0;
  B.Z=8.4;
  //se define la partícula que estará en el campo magnético
  particle particula;
  particula.setvalues(3.4, 0.0, 0.0, 0.0, 3.0, 0.0, 5.0, 1); 


  //se calculan las componentes del campo magnético y su respectiv   
  while ( t <= 10)
   {
    float AX = particula.Carga * (particula.VY*B.Z-B.Y*particula.VZ )/particula.M;
    float AY = particula.Carga * (-particula.VX*B.Z+B.X*particula.VZ)/particula.M;
    float AZ = particula.Carga * (particula.VX*B.Y-B.X * particula.VY)/particula.M; 
    cout << particula.X << " " << particula.Y << " " << particula.Z << endl;
    particula.pos_evol(AX, AY, AZ, dt); //se evoluciona la posición del sistema
    particula.vel_evol(AX, AY, AZ, dt); //se evoluciona la velocidad del sistema
    t=t+dt;
   }
  return 0;
}
