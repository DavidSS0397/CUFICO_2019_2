/*El siguiente programa se utiliza para describir la evolución de una partícula cargada sometida a un campo magnético constante. */

#include <iostream>
using namespace std;

//Se define una clase que permita caracterizar a la partícula que se va a estudiar.  

class Particle
{
public:
int Carga;
float X,Y,Z; //Posiciones
float VX ,VY,VZ; //Velocidades
float M; //Masa

//Se realiza un método para la clase, éste va a recibir los valores correspondientes a la partícula   
void Setvalues(float,float,float,float,float,float,float,int);
  
float Pos_evol(float,float,float,float);

} ;

//Para poder hacer uso de los métodos de la clase, primero debe especificarse lo que va a hacer cada uno de ellos y atribuirlos a la clase.

void Particle::Setvalues(float x ,float y, float z, float vx, float
			 vy, float vz, float m, int carga)
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

float Particle::Pos_evol(float Bx,float By, float Bz, float dt)
{
  //Como el sistema trabaja con ecuaciones diferenciales, lo que se hace es un proceso iterativo, para ello sirve el for y con un paso de tiempo pequeño

  for (int i=0;i<100000;i++)
{
  
float ax=(Carga/M)*(VY*Bz-VZ*By);
float ay=(Carga/M)*(VZ*Bx-VX*Bz);
float az=(Carga/M)*(VX*By-VY*Bx);
 
VX=VX+ax*dt;
VY=VY+ay*dt;
VZ=VZ+az*dt;

X=X+(VX*dt)+(0.5*ax*(dt*dt));
Y=Y+(VY*dt)+(0.5*ay*(dt*dt));
Z=Z+(VZ*dt)+(0.5*az*(dt*dt));
}
}


int main()
{
  //Se define la instancia de la clase
Particle Particula;

/*En las siguientes líneas se presentan dos situaciones "Condiciones de prueba" trabaja con un campo magnético únicamente en la dirección Z y una velocidad inicial de la partícula sólo en la dirección X, lo que lleva a que, como la partícula tiene carga positiva, su movimiento se restrinja al plano X-Y (VZ=0) y que para las primeras iteraciones, la posición en Y sea negativa. Las segundas condiciones corresponden a un caso general.
Es importante anotar que la precisión de los datos está altamente limitado por el número de iteraciones y la elección del paso de tiempo.  */
 
Particula.Setvalues(0.0,0.0,0.0,1.0,0.0,0.0,1.0,1);
 
 cout << "Condiciones de prueba. "<< endl;
 
Particula.Pos_evol(0.0,0.0,1.0,0.001);
 
cout <<"Posiciones:" <<" " << Particula.X << " "<< Particula.Y
<< " "<<Particula.Z << " "<< endl;
 
 cout <<"Velocidades: "<< " " << Particula.VX <<" " << Particula.VY << " "
<< Particula.VZ << " "<< endl;

Particula.Setvalues(2.0,1.0,3.0,1.0,5.0,9.0,1.0,-1);
 
 cout << "Condiciones generales. "<< endl;
 
Particula.Pos_evol(1.0,1.0,1.0,0.0001);
 
cout <<"Posiciones:" <<" " << Particula.X << " "<< Particula.Y
<< " "<<Particula.Z << " "<< endl;
 
 cout <<"Velocidades: "<< " " << Particula.VX <<" " << Particula.VY << " "
<< Particula.VZ << " "<< endl;


 return 0;
}
